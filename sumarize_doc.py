from openai import OpenAI
def summarize_doc(openai_api_key,document):
 
    client = OpenAI(api_key=openai_api_key)
    prompt = f"""
                You are an expert Document processor summarize the following document by providing an overview of its content and structure. The summary should follow the document hierarchy, including headings . Ensure that each heading  is clearly identified and that the key points or information under each are briefly described.

                Example Format:

                Heading 1
                Key points/information

                Heading 2
                Key points/information

      document: {document}
    """
   
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content":prompt
        }
    ])
    
    tokens_used = response.usage.total_tokens
    response = response.choices[0].message.content
    print("RESPONSE :",response)
    print("TOKENS USED IN THIS CALL : ",tokens_used)
    return response,tokens_used

