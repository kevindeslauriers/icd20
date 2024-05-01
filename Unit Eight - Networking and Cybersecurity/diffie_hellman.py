G = 7
P = 43

a_secret = int(input("What is Alice's Secret Key? "))
b_secret = int(input("What is Bob's Secret Key? "))

A = G**a_secret % P
B = G**b_secret % P

print()
print(f"Bob will send {B} to Alice")
print(f"Alice will send {A} to Bob")

alice_shared_secret = B**a_secret % P
print(f"The shared secret that Alice worked out is {alice_shared_secret}")

bob_shared_secret = B**a_secret % P
print(f"The shared secret that Bob worked out is {bob_shared_secret}")


