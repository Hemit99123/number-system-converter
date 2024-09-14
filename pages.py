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

    def convertDecimalToBinary(decimal):
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

def page_three():
    st.title('Hexadecimal to Binary Converter')
    st.write('Hexadecimal makes it easier to understand Binary code as it can get pretty long! Here is a quick program to help you :)')
    def convertHexadecimaltoBinary(hex):
        ref = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }
        binary_output = ""
        hex = hex
        for i in hex:
            if i.upper() in ref:
                binary_output = binary_output + ref[i.upper()]
            else:
                return "Invalid Base-16 integer (can only include 0-9, A-F)"
        return binary_output
    
    # Input component: Text Input
    hex = st.text_input("Enter Hex (Base-16) integer:")

    # Button component
    if st.button('Submit'):
        # When the button is clicked, display the input
        st.text("Base-10 (decimal) number:")
        st.write(convertHexadecimaltoBinary(hex=hex))