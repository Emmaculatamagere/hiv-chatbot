from flask import Flask, request,jsonify

app = Flask(__name__)

hcb = {
        "ukimwi ni nini":"ukimwi ni upungufu wa kinga mwilini",
        "vvu ni nini":"vvu ni virusi vinavyosababisha ukimwi",
        "ukimwi ulianza lini":"ukimwi uligundulika mnamo mwaka 1981 huko marekani",
        "vvu vinapelekeaje ukimwi":"vvu huharibu kinga ya mwili kwa kuingia na kuzaliana kwenye chembe za kinga za mwili kumfanya mtu apate ukimwi na magonjwa ya mkupuo",
        "dalili za ukimwi ni zipi":"kukonda sana, kutokwa na vidonda mdomoni, kutokwa na jasho sana hasa wakati wa usiku,kukohoa,kuharisha,kupata magonjwa mengi kwa mkupuo" ,
        "dalili za ukimwi zinaonekana muda gani baada ya kupata vvu":"hii inategemeana na mtu lakini muda wastani ni miaka nane hadi kumi",
        "nitajuaje nina ukimwi":"unatakiwa kupima damu katika kituo cha afya kilicho karibu",
        "napataje ukimwi":"majimaji ya mwili wako kama damu yanapogusana na majimaji ya mwili wa muathirika", 
        "je ukimwi una tiba":"ukimwi hauna tiba ila una dawa ya kupunguza makali ya hivyo virusi",
        "naepukaje kupata ukimwi":"kuwa muaminifu kwenye mahusiano,kuacha ngono zembe,kuepuka kushirikiana vitu vyenye ncha kali na kujilinda wakati wa kusaidia watu wenye vidonda",
        "nifanye nini baada ya kuathirika":"kula matunda na mbogamboga kwa sana, fanya mazoezi, kunywa maji kwa wingi na tumia dawa za kupunguza makali ya vvu"
        }

@app.route("/n", methods = ["GET","POST"])
def ask():
    question = request.get_json()["question"].lower().replace("?"," ").strip()
    return hcb[question]       