import numpy as np, pandas as pd
from scipy import stats as sa
import streamlit as st

def european_pricing(para, option_type='call'):
    S, K, T, r, sigma, _ = para
    d1= (np.log(S/K) + (r + 0.5* sigma**2)*T) / (sigma * np.sqrt(T))
    d2= d1 - sigma*np.sqrt(T)

    if option_type == 'call':
        call_price = S*sa.norm.cdf(d1) - K*np.exp(-r*T)* sa.norm.cdf(d2)   
        return (call_price)
    
    elif option_type == 'put':
        put_price =  K*np.exp(-r*T)* sa.norm.cdf(-d2) - S*sa.norm.cdf(-d1)  
        return (put_price)
    else:
        return ValueError('Invalid Option Selection')
    
def main():
    para = []
    st.title('Eurpean Option Pricing App')
    st.sidebar.header('Input Parameters')
    S= st.sidebar.number_input("Current Stock Price", min_value=0.00, value=100.00, step=0.1)
    K= st.sidebar.number_input("Strike Price", min_value=0.00, value=100.00, step=0.1)
    T= st.sidebar.number_input("Time to maturity (in years)", min_value=0.0001, value=0.0005, step=0.001)
    r= st.sidebar.number_input("Risk free Interest Rate", min_value=0.0001, value=0.0005, step=0.0001, format="%.4f")
    sigma= st.sidebar.number_input("Volatility", min_value=0.000, value=0.020, step=0.001, format="%.4f")
    type = st.sidebar.selectbox('Option Type', ['Call', 'Put'])
    para = [S, K, T, r, sigma, type]

    result= european_pricing(para, type.lower())

    st.header ('Option Pricing Result')
    st.info(result)

if __name__ == '__main__':
    main()