import streamlit as st

def page_one():
    st.title('Binary To Decimal Converter')
    
    def convertBinaryToDecimal(binary):
        l = list(binary)[::-1]
        output = 0

        for i in range(len(l)):
            if l[i] == "1":
                output += 2**int(i)
            elif l[i] != "0":
                return "Not a Base-2 integer"
        
        return output

    # Input component: Text Input
    binary = st.text_input("Enter Binary (Base-2) integer:")

    # Button component
    if st.button('Submit'):
        # When the button is clicked, display the input
        st.text("Base-10 (decimal) number:")
        st.write(convertBinaryToDecimal(binary=binary))


def page_two():
    st.title('Decimal to Binary Converter')

    def convertDecimalToBinary(decimal: int):
        decimal = int(decimal)
        output = ""
        while decimal > 0:
            output = str(decimal % 2) + output
            decimal = decimal // 2
        return output

    # Input component: Text Input
    decimal = st.text_input("Enter Decimal (base-10) integer:")

    # Button component
    if st.button('Submit'):
        # When the button is clicked, display the input
        st.text("Base-2 (binary) number:")
        st.write(convertDecimalToBinary(decimal=decimal)) 
