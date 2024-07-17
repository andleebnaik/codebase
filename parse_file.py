from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
import os

def parser(filename):
    narrative_text =""
    title_text = ""
    title_collected = False
    narrativetxt_collected = False
    document_dictionary = {}
    os.environ["UNSTRUCTURED_API_KEY"] = "5uraRltawpgEtQbSF42MYnbcBLO2vy"
    unstructured_api_key = os.environ.get("UNSTRUCTURED_API_KEY")
    
    client = UnstructuredClient(
        api_key_auth=unstructured_api_key,
        # if using paid API, provide your unique API URL:
        # server_url="YOUR_API_URL",
    )

    # Update here with your filename

    with open(filename, "rb") as f:
        files=shared.Files(
            content=f.read(),
            file_name=filename,
        )

   # hi_res or ocr_only for strategy
    req = shared.PartitionParameters(files=files, strategy="hi_res",coordinates=True)

    try:
        resp = client.general.partition(req)
        for element in resp.elements:
            print("TEXT : ",element["text"])
            print("TYPE : ",element["type"])

            if element["type"]== "Title":
                if title_collected ==True:
                    document_dictionary[title_text] = narrative_text 
                    title_text = ""
                    narrative_text =""
                    title_collected = False
                    narrativetxt_collected = True
                    title_text= title_text + element["text"] 
                if narrativetxt_collected == False:
                    title_text = title_text + element["text"]        
                    if element == resp.elements[-1]:
                       document_dictionary[document_dictionary[title_text] + element["text"]] = ""

            elif element["type"] == "NarrativeText":
                title_collected = True

                narrative_text = narrative_text + element["text"]
                
                
                if element==resp.elements[-1]:
                    document_dictionary[title_text] = narrative_text
                
                    narrativetxt_collected = True
        #print("DOCUMENT : ",document_dictionary)
        for key, value in document_dictionary.items():
                print(f"{key}  :  {value}")
                print("\n")
        return document_dictionary 
    except SDKError as e:
        print(e)