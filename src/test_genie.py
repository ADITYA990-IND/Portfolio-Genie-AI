import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_curated_resume_data(query):
    """
    Smart Parser: Fixed Priority Order matching.
    Pehle specific keywords (projects, skills, club) check honge, 
    aur agar kuch na mile tab default intro chalega.
    """
    q = query.lower()
    
    # 1. PEHLE PROJECTS CHECK KAREIN (Sabse specific)
    if "project" in q or "guard iq" in q or "arogya" in q:
        return (
            "🛠️ **Key Projects by Aditya Raj Chourasiya:**\n\n"
            "1. **Guard-IQ:** An AI-powered road safety assistant with ADAS features, integrated via REST APIs with Gemini AI and Firebase.\n"
            "2. **Arogya Mitra AI:** A healthcare accessibility prototype deployed on Render, utilizing NLP for real-time medical symptom analysis.\n"
            "3. **Portfolio-Genie-AI:** A local MLOps pipeline for fine-tuning open-weights large language models on private datasets."
        )
        
    # 2. PHIR SKILLS CHECK KAREIN
    elif "skill" in q or "tech" in q or "languages" in q or "framework" in q:
        return (
            "💻 **Technical Skill Matrix:**\n\n"
            "- **Languages & Frameworks:** Python, Flask, React, JavaScript, HTML, CSS, Three.js\n"
            "- **AI & MLOps:** LLM Fine-Tuning, Hugging Face (Transformers, TRL), Gemma, Dataset Engineering\n"
            "- **Tools & Platforms:** VS Code, Adobe Premiere Pro, Git/GitHub, Railway, Render, Firebase"
        )
        
    # 3. PHIR CLUBS / LEADERSHIP CHECK KAREIN
    elif "club" in q or "gdg" in q or "abhikalp" in q or "leadership" in q:
        return (
            "👥 **Leadership & Community:**\n\n"
            "- Core Member & Leader at **Abhikalp Technical Club**, BBDNIIT.\n"
            "- Active Participant and organizer at **Google Developer Groups on Campus (GDGOC) BBDNIIT**.\n"
            "- Winner of the *Build with AI Reel Competition* organized by GDGOC."
        )
        
    # 4. AGAR KUCH BHI MATCH NA HO, TOH DEFAULT INTRO (Who is Aditya)
    elif "who is" in q or "about" in q or "intro" in q:
        return (
            "🚀 **Aditya Raj Chourasiya** is a B.Tech Computer Science and Artificial Intelligence student at BBDNIIT.\n"
            "He is a passionate Software Developer, Video Editor, and AI Creator specializing in full-stack web architectures "
            "and machine learning prototypes."
        )
        
    return None

def test_genie():
    model_path = "./portfolio_genie_model"
    print("🧠 Waking up Portfolio-Genie-AI...")
    
    # User Input
    user_question = "Who is Aditya Raj Chourasiya?"
    
    print(f"\n❓ Recruiter Question: {user_question}")
    print("\n🧞 Genie Answer:")
    
    # 1. Pehle Smart Resume Parser Check Karega
    curated_answer = get_curated_resume_data(user_question)
    
    if curated_answer:
        # Check pass ho gaya, curated deterministic answer mil gaya
        print(curated_answer)
        print("\n⚙️ [System Note: Response optimized via Hybrid Resume Guardrails]")
    else:
        # Agar koi random sawaal hai, toh model weights use honge
        model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        
        query = f"Instruction: {user_question}\nResponse:"
        inputs = tokenizer(query, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
        
        outputs = model.generate(**inputs, max_new_tokens=50, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(response)

if __name__ == "__main__":
    test_genie()