guests = ['Nelson Mandela', 'Stephen Curry', 'Eden Hazard']

print(f"Dear {guests[0]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[1]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[2]}, you are invited to dinner on Saturday.")


print(f"\n{guests[0]} cannot make it to dinner.\n")

guests[0] = 'Kwame Nkrumah'

print(f"Dear {guests[0]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[1]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[2]}, you are invited to dinner on Saturday.")

print("\n I have found a bigger table for dinner so inviting more guests\n")

guests.insert(0, 'Isaac Newton')
guests.insert(2, 'Yaa Asantewaa')
guests.append('Ella Mai')

print(f"Dear {guests[0]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[1]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[2]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[3]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[4]}, you are invited to dinner on Saturday.")
print(f"Dear {guests[5]}, you are invited to dinner on Saturday.")


print(f"\n Another update, I can now invite only two guests\n")

sixth_guest = guests.pop()
print(f"Hello {sixth_guest}, sorry I cannot invite you to dinner")
fifth_guest = guests.pop()
print(f"Hello {fifth_guest}, sorry I cannot invite you to dinner")
fourth_guest = guests.pop()
print(f"Hello {fourth_guest}, sorry I cannot invite you to dinner")
third_guest = guests.pop()
print(f"Hello {third_guest}, sorry I cannot invite you to dinner")

print(f"\nDear {guests[0]}, you are still invited to dinner on Saturday.")
print(f"Dear {guests[1]}, you are still invited to dinner on Saturday.")


del guests[0:2]
print(guests)