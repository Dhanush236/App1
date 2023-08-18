{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "155d4094",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "import numpy as np\n",
    "pickle_in=open('hdp.pkl','rb')\n",
    "clf=pickle.load(pickle_in)\n",
    "\n",
    "def main():\n",
    "    html_temp='''\n",
    "    <div style=\"background-color:yellow;padding:13px\">\n",
    "    <h1 style=\"color:black;text-align:center;\">CORONARY HEART DETECTION PREDICTION</h1>\n",
    "    </div>'''\n",
    "\n",
    "    st.markdown(html_temp,unsafe_allow_html=True)\n",
    "    age=st.number_input(\"AGE\")\n",
    "    sex=st.number_input(\"Sex\")\n",
    "    cpt=st.number_input(\"Chest pain type\")\n",
    "    bp=st.number_input('BP')\n",
    "    chp=st.number_input('Cholesterol')\n",
    "    fbs=st.number_input('FBS over 120')\n",
    "    ekg=st.number_input('EKG results')\n",
    "    hr=st.number_input('Max HR')\n",
    "    ea=st.number_input('Exercise angina')\n",
    "    std=st.number_input('ST depression')\n",
    "    sst=st.number_input('Slope of ST')\n",
    "    vf=st.number_input('Number of vessels fluro')\n",
    "    t=st.number_input('Thallium')\n",
    "\n",
    "    result=''\n",
    "\n",
    "    if st.button('PREDICT'):\n",
    "        result=prediction(age,sex,cpt,bp,chp,fbs,ekg,hr,ea,std,sst,vf,t)\n",
    "        st.success('RISK IS {}'.format(result))\n",
    "\n",
    "def prediction(age,sex,cpt,bp,chp,fbs,ekg,hr,ea,std,sst,vf,t):\n",
    "    s=clf.predict([[age,sex,cpt,bp,chp,fbs,ekg,hr,ea,std,sst,vf,t]])\n",
    "    if s==1:\n",
    "        p='Presence'\n",
    "    else:\n",
    "        p='Absence'\n",
    "    return p\n",
    "\n",
    "if __name__=='__main__':\n",
    "    main()\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
