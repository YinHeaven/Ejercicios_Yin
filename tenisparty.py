


def tenis_party(player1, player2):
    while True:  # Bucle infinito
        if player1 == 0 and player2 == 0:
            return "love - love"  # Ambos jugadores tienen 0 puntos
        elif player1 == 0:
            return f"love - Player 2: {player2}"  # Player 1 tiene 0 puntos
        elif player2 == 0:
            return f"Player 1: {player1} - love"  # Player 2 tiene 0 puntos
        elif player1 == player2:
            return "deuce - deuce"  # Ambos jugadores tienen el mismo puntaje
        elif player1 > player2:
            return f"Player 1: {player1} - Player 2: {player2}"  # Player 1 tiene más puntos
        else:
            return f"Player 1: {player1} - Player 2: {player2}"  # Player 2 tiene más puntos

def ganador(player1, player2):
    if player1 == 40 or player  # type: ignore
    if player1 > player2:
        return "Player 1 winner"
    elif player2 > player1:
        return "Player 2 winner"
    else:
        return "Deuce (es un empate)"  # Empate

# Solicitar puntos de los jugadores
player1 = int(input("Enter point of player 1: "))
player2 = int(input("Enter point of player 2: "))
print(tenis_party(player1, player2))

player1 = int(input("Enter point of player 1: "))
player2 = int(input("Enter point of player 2: "))
print(tenis_party(player1, player2))

player1 = int(input("Enter point of player 1: "))
player2 = int(input("Enter point of player 2: "))
print(tenis_party(player1, player2))

player1 = int(input("Enter point of player 1: "))
player2 = int(input("Enter point of player 2: "))
print(tenis_party(player1, player2))

player1 = int(input("Enter point of player 1: "))
player2 = int(input("Enter point of player 2: "))
print(tenis_party(player1, player2))

# Llamar a la función


input("Press Enter to exit...")




