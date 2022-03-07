# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text. ")

# # when the file is not exited, use mode "w" will create it
# with open("new_file.txt", mode = "w") as file:
#     file.write("New text. ")