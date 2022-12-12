from flask import Flask, render_template, request
import os
from modules import filehandling as fh

app = Flask(__name__, static_url_path='/static')


@app.route('/',methods=['GET'])
def home():
    return "working <a href='/XSD' target='_blank'>XSD</a>, <a href='/xmlHandling' target='_blank'>xml handling</a>"

@app.route('/xmlHandling',methods=['GET'])
def xml():
    return render_template('index.html')

@app.route('/xmlHandling/XML', methods=['GET','POST'])
def XML_handling():
    if request.method == "GET" or request.method=='POST':
        path = str(request.form.get("path"))
        search_text = 'name="' + str(request.form.get("element")) + '"'

        # search_text = 'name="RISchCGMTbl"'
        # path = "C:\Django Projects\RIBusiness2022V.02"
        # schema_path = "\Schemas"

        xsd_files = fh.get_list_of_files(path,".xsd")
        xml_files = fh.get_list_of_xml_files()
        if len(xml_files) != 0:
            fh.removefiles(xml_files)
        fh.convert_xsd_to_xml_files(path)
        #new_xmls = fh.get_list_of_xml_files()
        result1 = fh.search_for_text(search_text)
        result = xsd_files[len(result1)-1]

        #return path + search_text
        #return "working"
        return result
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(debug=False, port=port)
    #app.run()
    app.run(debug=False, host='0.0.0.0')
