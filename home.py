import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
        page_title="AAYU",
        page_icon="logo.jpg",
        layout="centered"
)

def app():

    
    st.title("Image Classification")
    st.sidebar.subheader("Input")

    models_list = ["MobileNetV2"]
    selected_model = st.sidebar.selectbox("Select the Model", models_list)

    MODELS = {
        "MobileNetV2": 'Model.h5',
    }

    uploaded_file = st.sidebar.file_uploader(
        "Choose an image to classify", type=["jpg", "jpeg", "png"]
    )

    
    if uploaded_file is None:
        img = Image.open('logo.jpg')
        img = img.resize((450,450))
        st.image(img)
    else:
        model = tf.keras.models.load_model('Model.h5')
        class_names = { 0:'Aloevera',
                1:'Amaranthus Viridis (Arive - Dantu)',
                2:'Amruthabali',
                3:'Arali',
                4:'Castor',
                5:'Mango',
                6:'Mint',
                7:'Neem',
                8:'Sandalwood',
                9:'Turmeric'
                }
       

        img = Image.open(uploaded_file)
        img = img.resize((224, 224))

        
        img_pred = Image.open("test6.jpg")
        img_pred = img_pred.resize((224,224))
        img_pred = np.asarray(img_pred)

        img_pred=img_pred/255.
    
        predictions = model.predict(img_pred)
        prediction = predictions.argmax()
        prob = predictions[0][prediction]
        
        confidence_score = prob*100
        confidence_score = round(confidence_score, 2)
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, channels="RGB")
       
        with col2:
            st.header(class_names[prediction])
            st.text("According to model Prediction \n{}% this is the Image of {}".format(confidence_score,class_names[prediction]))
        data(class_names[prediction]) 



def data(output):
    if output == "Aloevera":
        st.header("Desciption...")
        st.text("""
                Aloe vera is a cactus-like plant that has been used for centuries for 
                its health, beauty, medicinal, and skin care properties. Its useful 
                parts are the gel and latex. Aloe gel might help some skin conditions like 
                psoriasis, speed up wound healing by improving blood circulation, and might 
                combat certain types of bacteria and fungi. Aloe vera is the only edible form 
                of aloe and is native to the Arabian peninsula but grows throughout the world. 
                It has been used to heal a variety of conditions, most notably burns, wounds, 
                skin irritations, and constipation. Aloe was one of the most frequently prescribed 
                medicines throughout most of the 18th and 19th centuries and remains one of the 
                most commonly used herbs in the United States today.""")
        st.header("Health Benifits....")
        st.text("""
                1. Skin Health: Soothes and moisturizes, aiding in sunburn and minor burn relief.
                2. Digestive Aid: Aloe vera juice may promote bowel regularity and alleviate IBS symptoms.
                3. Anti-Inflammatory: Contains compounds that reduce inflammation in the body.
                4. Joint and Muscle Health: Anti-inflammatory properties contribute to pain relief.
                5. Nutrient-Rich: A source of vitamins, minerals, and amino acids.
                6. Hair and Scalp Health: Aloe vera gel moisturizes hair, reduces dandruff,
                """)
        
    if output == "Amaranthus Viridis (Arive - Dantu)":
        st.header("Desciption...")
        st.text("""
                Amaranthus viridis, or Arive-Dantu, is a versatile leafy green used in salads and 
                stir-fries, rich in vitamins A and C, iron, and calcium. Cultivated in Asia and Africa, 
                it holds cultural significance and is valued for its nutritional content. Beyond its 
                culinary uses, Amaranthus viridis is explored for potential medicinal benefits, including 
                antioxidant and anti-inflammatory properties. Easy to grow, it adapts well to different 
                soils, but caution is advised due to potential invasiveness in certain species.""")
        st.header("Health Benifits....")
        st.text("""
                1. Nutrient-Rich: Amaranthus viridis is abundant in vitamins A and C, iron, and calcium.
                2. Vitamin A for Eye Health: Presence of vitamin A contributes to maintaining good vision.
                3. Weight Management: Dietary fiber may aid in weight management and controlling appetite.
                4. Immune System Support: The vitamins and minerals present contribute to a strengthened 
                   immune system.
                """)
    if output == "Amruthabali":
        st.header("Desciption...")
        st.text("""
                Amruthabali is a traditional Ayurvedic herbal preparation known for its potential health
                benefits. Comprising a blend of herbs and natural ingredients, it is believed to promote 
                overall well-being, vitality, and immunity. Typically administered orally, Amruthabali is 
                used in Ayurveda for rejuvenation and to enhance general health. It's essential to use 
                this preparation under the guidance of a qualified Ayurvedic practitioner due to variations 
                in composition and individual responses.""")
        st.header("Health Benifits....")
        st.text("""
                1. Well-being Boost: Amruthabali is believed to enhance overall health and vitality.
                2. Immunity Support: It may have properties that support and strengthen the immune system.
                3. Rejuvenation: Commonly used in Ayurveda for rejuvenating the body and promoting longevity.
                4. Natural Ingredients: Composed of herbs and natural ingredients based on Ayurvedic principles.
                5. Guided Usage: Should be used under the guidance of a qualified Ayurvedic practitioner for 
                   optimal benefits.
                """)
        
    if output == "Arali":
        st.header("Desciption...")
        st.text("""
                The Arali plant, part of the Araliaceae family, encompasses a diverse range of plants, 
                including trees, shrubs, and herbs. Common features include compound leaves, small flowers, 
                and berries. Examples include Aralia spinosa (Devil's Walking Stick) and Panax ginseng 
                (Ginseng). The family serves various purposes, with some species like ginseng having medicinal 
                uses, while others are valued for ornamental or cultural reasons.""")
        st.header("Health Benifits....")
        st.text("""
                1. Ginseng (Panax ginseng): Adaptogenic, immune support, cognitive enhancement, antioxidant.
                2. Aralia spinosa (Devil's Walking Stick): Limited medicinal use, potential antioxidant benefits.
                3. General Araliaceae Family: Varied species, potential anti-inflammatory properties, ornamental 
                   varieties contribute to aesthetics.
                """)
        
    if output == "Castor":
        st.header("Desciption...")
        st.text("""
                The castor plant, scientifically known as Ricinus communis, is a robust and rapidly growing shrub 
                native to tropical regions. Recognizable for its large palmate leaves, some of which may display a 
                distinctive red hue, the plant produces spiky capsules containing seeds. Notably, these seeds are 
                the source of castor oil, a versatile substance with applications in industry, medicine, and cosmetics. 
                While castor oil is prized for its beneficial properties, it's important to exercise caution as the 
                seeds themselves are toxic if ingested and should be handled with care.""")
        st.header("Health Benifits....")
        st.text("""
                1. Antimicrobial Properties: Some studies suggest it may have antimicrobial effects.
                2. Wound Healing: Applied to wounds for potential healing benefits.
                3. Skin Moisturization: Used in cosmetics for its moisturizing properties.
                4. Anti-Inflammatory: Applied topically, it may help reduce inflammation.
                """)
        
    if output == "Mango":
        st.header("Desciption...")
        st.text("""
                The mango, scientifically known as Mangifera indica, is a tropical stone fruit 
                characterized by its large, oval shape and smooth skin. Ranging in color from 
                green to yellow, orange, or red when ripe, the mango is renowned for its sweet and 
                juicy flesh, featuring a distinctive tropical flavor. The fruit houses a large, 
                flat seed in its center. Rich in vitamins (C, A), fiber, and antioxidants, mangoes 
                are enjoyed fresh, in smoothies, salads, or as part of various culinary delights. 
                With numerous varieties, such as Alphonso, Haden, and Keitt, mangoes hold cultural 
                significance, being widely cultivated and cherished across the globe.""")
        st.header("Health Benifits....")
        st.text("""
                1. Antioxidants: Packed with antioxidants that help combat oxidative stress in the body.
                2. Rich in Vitamins: Abundant in vitamin C for immune support and vitamin A for eye health.
                3. Hydration: High water content contributes to hydration.
                4. Nutrient-Rich: Provides essential nutrients like potassium, magnesium, and folate.
                5. Anti-Inflammatory: Contains compounds with potential anti-inflammatory effects.
                6. Heart Health: Potassium content supports heart health by helping regulate blood pressure.

                """)
        

    if output == "Mint":
        st.header("Desciption...")
        st.text("""
                Mint, a fragrant herb with the botanical name Mentha, is widely recognized for its aromatic 
                leaves and versatile uses. Commonly found in various culinary and medicinal applications, mint 
                leaves are known for their refreshing flavor, often used in teas, salads, and desserts. The herb 
                is easy to cultivate, thriving in diverse climates. Beyond its culinary appeal, mint is valued 
                for its potential health benefits, including digestive support, headache relief, and its antimicrobial 
                properties. Its invigorating scent and cooling sensation make it a popular choice for both culinary 
                and wellness purposes.
                """)
        st.header("Health Benifits....")
        st.text("""
                1. Digestive Aid: Mint can help alleviate indigestion and soothe an upset stomach.
                2. Headache Relief: The menthol in mint may provide relief from headaches and migraines.
                3. Respiratory Health: Menthol's decongestant properties can ease respiratory issues.
                4. Antimicrobial Properties: Mint has natural antimicrobial and antibacterial qualities.
                5. Improved Focus and Alertness: The invigorating scent of mint is believed to enhance mental clarity and concentration.
                6. Skin Health: Mint-infused products or applications may soothe skin irritation.
                7. Calming Effects: Mint tea or aromatherapy can have a calming effect, reducing stress.
                8. Weight Management: The aroma of mint may help control appetite and aid in weight management.
                """)
        

    if output == "Neem":
        st.header("Desciption...")
        st.text("""
                Neem, scientifically known as Azadirachta indica, is a versatile tree native to the Indian 
                subcontinent. Renowned for its numerous medicinal and agricultural applications, neem is characterized by 
                evergreen leaves and small, fragrant white flowers. Extracts from neem, particularly neem oil, 
                are valued for their potent antimicrobial and insecticidal properties. In traditional medicine, 
                neem is hailed for its potential to treat various ailments, ranging from skin conditions to digestive 
                issues. Widely cultivated for its wide-reaching benefits, neem continues to play a significant role in 
                herbal medicine, agriculture, and personal care products.
                """)
        st.header("Health Benifits....")
        st.text("""
                1. Antibacterial and Antiviral Properties: Neem is known for its potent antibacterial and antiviral effects.
                2. Skin Health: Used in skincare for conditions like acne and eczema due to its anti-inflammatory properties.
                3. Oral Health: Neem-based oral care products may contribute to dental health and reduce gum issues.
                4. Antioxidant Effects: Neem contains compounds with antioxidant properties, combating oxidative stress.
                5. Immune System Support: Its immune-boosting properties may contribute to overall health.
                6. Digestive Aid: Traditionally used to address digestive issues and promote gut health.
                """)
        

    if output == "Sandalwood":
        st.header("Desciption...")
        st.text("""
                Sandalwood, derived from the fragrant heartwood of Santalum trees, is esteemed for its distinctive 
                aroma and diverse applications. Renowned in the perfume industry for its rich, woody scent, sandalwood 
                is also valued for its use in traditional medicine, skincare, and religious rituals. The heartwood's 
                essential oil is known for its calming properties and is often used in aromatherapy. Sandalwood paste 
                has been utilized for centuries in skincare routines, believed to promote smooth and radiant skin. 
                Additionally, sandalwood holds cultural significance in various traditions and is often used in religious 
                ceremonies and meditation practices.
                """)
        st.header("Health Benifits....")
        st.text("""
                1. Aromatherapy: Calming and stress-reducing effects.
                2. Skincare: Anti-inflammatory, antiseptic properties for skin health.
                3. Antioxidant: Combats free radicals in the body.
                4. Astringent: Tightens and tones the skin.
                5. Mood Enhancement: Enhances mood and mental clarity.
                6. Relaxation: Contributes to relaxation and potentially better sleep.
                """)
        

    if output == "Turmeric":
        st.header("Desciption...")
        st.text("""
                Turmeric, derived from the Curcuma longa plant, is a golden-hued spice celebrated for its vibrant 
                color and versatile uses. Widely known for its active compound, curcumin, turmeric has been a staple 
                in traditional medicine for its potential health benefits. Beyond its culinary applications, turmeric 
                is revered for its anti-inflammatory and antioxidant properties, contributing to joint health and overall 
                well-being. It is a key ingredient in various cuisines, and its presence in teas, supplements, and skincare 
                products highlights its diverse role in promoting both culinary delight and potential health support.
                """)
        st.header("Health Benifits....")
        st.text("""
                1. Anti-Inflammatory: Curcumin reduces inflammation.
                2. Antioxidant: Rich in antioxidants, combating oxidative stress.
                3. Joint and Digestive Health: Supports joint health and aids digestion.
                4. Heart Health: May improve cholesterol levels.
                5. Brain Health: Potential neuroprotective properties.
                6. Anti-Cancer Potential: Preliminary research suggests inhibitory effects on certain cancer cells.
                7. Skin Conditions: Anti-inflammatory properties may benefit skin health.
                """)  


app()      

    
