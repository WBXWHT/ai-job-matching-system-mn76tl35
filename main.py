import json
import time
from datetime import datetime
from typing import List, Dict, Any

class AIJobMatchingSystem:
    """AI智能职位匹配与推荐系统"""
    
    def __init__(self):
        # 模拟微调的大模型参数
        self.model_params = {
            "model_name": "fine-tuned-bert",
            "version": "1.0",
            "similarity_threshold": 0.7
        }
        
        # 模拟用户数据存储
        self.user_profiles = {}
        # 模拟职位数据
        self.job_database = self._init_job_database()
        
    def _init_job_database(self) -> List[Dict[str, Any]]:
        """初始化模拟职位数据库"""
        return [
            {
                "id": "JD001",
                "title": "AI平台产品经理实习生-抖音研发",
                "company": "字节跳动",
                "department": "抖音研发",
                "requirements": ["AI产品设计", "用户需求分析", "项目管理", "数据分析"],
                "description": "负责AI平台产品规划与设计，参与抖音AI功能研发",
                "tags": ["AI", "产品经理", "抖音", "实习生"]
            },
            {
                "id": "JD002",
                "title": "机器学习算法工程师",
                "company": "字节跳动",
                "department": "AI Lab",
                "requirements": ["Python", "TensorFlow", "深度学习", "自然语言处理"],
                "description": "负责推荐算法研发与优化",
                "tags": ["算法", "机器学习", "深度学习", "NLP"]
            },
            {
                "id": "JD003",
                "title": "后端开发工程师",
                "company": "字节跳动",
                "department": "基础架构",
                "requirements": ["Go", "微服务", "分布式系统", "数据库"],
                "description": "负责高并发后端系统开发",
                "tags": ["后端", "Go", "分布式", "微服务"]
            }
        ]
    
    def analyze_resume(self, user_id: str, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        """分析用户简历，提取关键信息"""
        print(f"\n正在分析用户 {user_id} 的简历...")
        
        # 模拟大模型语义理解处理
        time.sleep(0.5)  # 模拟处理时间
        
        profile = {
            "user_id": user_id,
            "skills": resume_data.get("skills", []),
            "experience": resume_data.get("experience", ""),
            "education": resume_data.get("education", ""),
            "interests": resume_data.get("interests", []),
            "analysis_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.user_profiles[user_id] = profile
        print(f"简历分析完成，提取到 {len(profile['skills'])} 项技能")
        return profile
    
    def track_user_behavior(self, user_id: str, job_id: str, action: str):
        """追踪用户浏览行为"""
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {"behavior_log": []}
        
        if "behavior_log" not in self.user_profiles[user_id]:
            self.user_profiles[user_id]["behavior_log"] = []
        
        behavior_record = {
            "job_id": job_id,
            "action": action,
            "timestamp": datetime.now().isoformat()
        }
        
        self.user_profiles[user_id]["behavior_log"].append(behavior_record)
        print(f"记录用户行为: {user_id} -> {action} -> {job_id}")
    
    def calculate_similarity(self, user_profile: Dict[str, Any], job: Dict[str, Any]) -> float:
        """计算用户与职位的匹配度（模拟大模型语义匹配）"""
        # 模拟BERT模型语义相似度计算
        user_skills = set(user_profile.get("skills", []))
        job_requirements = set(job.get("requirements", []))
        
        # 计算技能匹配度
        if not job_requirements:
            return 0.0
            
        skill_match = len(user_skills & job_requirements) / len(job_requirements)
        
        # 模拟大模型综合评分（包含语义理解）
        base_score = skill_match * 0.7
        
        # 考虑用户兴趣和行为
        if "behavior_log" in user_profile:
            viewed_jobs = [log["job_id"] for log in user_profile["behavior_log"] if log["action"] == "view"]
            if job["id"] in viewed_jobs:
                base_score += 0.1  # 浏览过该职位，增加匹配度
        
        # 确保分数在0-1之间
        final_score = min(1.0, max(0.0, base_score))
        
        return round(final_score, 2)
    
    def recommend_jobs(self, user_id: str, top_n: int = 3) -> List[Dict[str, Any]]:
        """为用户推荐最匹配的职位"""
        if user_id not in self.user_profiles:
            print(f"用户 {user_id} 未找到简历信息")
            return []
        
        user_profile = self.user_profiles[user_id]
        print(f"\n正在为 {user_id} 生成个性化推荐...")
        
        # 为每个职位计算匹配度
        job_scores = []
        for job in self.job_database:
            score = self.calculate_similarity(user_profile, job)
            job_scores.append({
                "job": job,
                "score": score,
                "matched": score >= self.model_params["similarity_threshold"]
            })
        
        # 按匹配度排序
        job_scores.sort(key=lambda x: x["score"], reverse=True)
        
        # 返回前N个推荐
        recommendations = job_scores[:top_n]
        
        # 输出推荐结果
        print(f"\n=== 个性化职位推荐结果 ===")
        print(f"用户ID: {user_id}")
        print(f"使用模型: {self.model_params['model_name']}")
        print(f"匹配阈值: {self.model_params['similarity_threshold']}")
        print("-" * 40)
        
        for i, rec in enumerate(recommendations, 1):
            job = rec["job"]
            print(f"{i}. {job['title']} @ {job['company']}")
            print(f"   匹配度: {rec['score']:.0%}")
            print(f"   部门: {job['department']}")
            print(f"   关键要求: {', '.join(job['requirements'][:3])}")
            print()
        
        # 统计提升效果（模拟项目成果）
        baseline_ctr = 0.15  # 基准点击率
        improved_ctr = baseline_ctr * 1.18  # 提升18%
        print(f"预计效果提升:")
        print(f"  - 用户点击率: {baseline_ctr:.0%} → {improved_ctr:.0%} (+18%)")
        print(f"  - 投递效率提升: +30%")
        
        return recommendations
    
    def apply_job(self, user_id: str, job_id: str) -> bool:
        """模拟职位申请"""
        job = next((j for j in self.job_database if j["id"] == job_id), None)
        if not job:
            print(f"职位 {job_id} 不存在")
            return False
        
        print(f"\n✓ 用户 {user_id} 成功申请职位: {job['title']}")
        print(f"  申请时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  申请ID: APP{int(time.time())}")
        
        # 记录申请行为
        self.track_user_behavior(user_id, job_id, "apply")
        
        return True


def main():
    """主函数 - 系统演示"""
    print("=" * 50)
    print("AI智能职位匹配与推荐系统")
    print("=" * 50)
    
    # 初始化系统
    system = AIJobMatchingSystem()
    
    # 模拟用户简历数据
    user_resume = {
        "user_id": "STU2023001",
        "name": "张三",
        "skills": ["AI产品设计", "用户需求分析", "Python", "数据分析", "项目管理"],
        "experience": "1年产品实习经验，参与过AI项目",
        "education": "计算机科学本科",
        "interests": ["AI产品", "推荐系统", "用户体验"]
    }
    
    # 1. 分析简历
    profile = system.analyze_resume(user_resume["user_id"], user_resume)
    
    # 2. 模拟用户浏览行为
    system.track_user_behavior(user_resume["user_id"], "JD002", "view")
    system.track_user_behavior(user_resume["user_id"], "JD001", "view")
    
    # 3. 获取个性化推荐
    recommendations = system.recommend_jobs(user_resume["user_id"], top_n=2)
    
    # 4. 申请最匹配的职位
    if recommendations:
        top_job = recommendations[0]["job"]
        system.apply_job(user_resume["user_id"], top_job["id"])
    
    print("\n" + "=" * 50)
    print("系统演示完成")
    print("=" * 50)


if __name__ == "__main__":
    main()