from faker import Faker

fake = Faker()

# Example usage
fake_name = fake.name()
fake_address = fake.address()

print("Fake Name:", fake_name)
print("Fake Address:", fake_address)