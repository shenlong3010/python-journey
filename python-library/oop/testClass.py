#
class Parrot:
	# class attribute
	species = "bird"

	# instance attribute
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age

	# instance method
	def sing(self, song):
		return f"{self.name} sings {song}"

	def dance(self):
		return f"{self.name} is now dancing"

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print(f"Blu is a {blu.__class__.species}")
print(f"Woo is also a {woo.__class__.species}")

print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

print(blu.sing("Happy"))
print(blu.dance())
