import streamlit as st
import numpy as np
import pandas as pd
from game import get_random_value, validate

def main():
    menu = ["Play", "Instructions", "About"]
    option = st.sidebar.selectbox("Menu", menu)

    if option=="Play":
        st.write("This is Play")

    elif option=="Instructions":
        st.subheader("Instructions")
        psi = '|ψ>'
        board = np.array([[psi,psi,psi], [psi,psi,psi], [psi,psi,psi]])
        st.write('board:')
        st.dataframe(board)
        instruction_1 = """
        The above board represents the initial state of the game.
        |ф> represents the superposition state!
        Always, the user is given the chance to make the first move.
        [0> and |1> represent the piece chosen by the Computer and User respectively.
        However, unlike the classical tic tac toe, there's not a 100% probability that
        when computer/user make their move, it will result into their respective move.
        For eg, if user selects a piece, it's actually possible that the piece take the value of |ø> and not 11.
        This is the Quantum effect of Quantum Superposition in the Quantum Tic Tac Toe!
        The squares in the 3x3 grid (board) are numbered in the following manner as shown below:
        """

        st.write(instruction_1)
        board_numbering = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])
        st.dataframe(board_numbering)

        instruction_2 = """
        The user can select any space from the 3x3 grid using the selection menu as shown below and the,
        press the submit button.

        (Note: TO get back, select a value from the menu!)
        """
        st.write(instruction_2)
    
    else:
        st.subheader('About')
        st.write('Group project - Quantum informatics')
        st.subheader('Authors:')
        st.markdown("- Krzysztof Kocot")
        st.markdown("- Krzysztof Molski")
        st.markdown("- Mateusz Płonka")
        st.markdown("- Tomasz Sitek")
        st.markdown("- Michał Urbanek")
        st.balloons()

if __name__ == '__main__':
    main()