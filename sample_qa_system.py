import google.generativeai as genai
genai.configure(api_key="YOUR API KEY")
model=genai.GenerativeModel("gemini-2.5-flash")

def answers_questions(question, retreived_chunks):
    context="\n".join(retreived_chunks)
    prompt=f"""Answer only using provided context in files
               Context:{context} Question:{question}
               Answer:"""
    response = model.generate_content(prompt)
    
    return response.text