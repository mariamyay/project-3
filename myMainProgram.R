library(reticulate)
source("MyRClass.R")
source_python("myPythonClass.py")
## Create a test case ###
### Part 1 ###
# 1. Save the encrypted story from the secretstory.txt file as my_story, using one of your Python Helper Module functions.
my_story <- get_story_text()
# 2. Create an instance of CaesarsDecoder with my_story as its initial input. 
story <- CeasarsDecoder(my_story)
# 3. Print the decrypted message of my_story.
print(story$decrypt_message()[2])
### Part 2 ### 
# 4. Create a variable called my_new_story and let it be equal to a story of your choice. Save it as a string.
my_new_story <- "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. - Steve Jobs"
# 5. Create an instance of AnytextMessage and with my_new_story and the shift of your choice as its inputs. 
new_decr_story <- AnytextMessage(my_new_story, 4L)
# 6. Use one of the AnytextMessage methods to encrypt my_new_story.
result <- new_decr_story$get_encr_msg()
print(result)
# 7. Save the output of the encryption in a text file called: "mysecretstory.txt"
scrt<-file("mysecretstory.txt")
writeLines(result, scrt)
close(scrt)
### Part 3 ###
# 8. Create an instance of the employee object called john with the name "John" of boss ("Mr. X" of age 52 - who is a Person object) and a salary of 100.
john <- new("Employee",
            name="John",
            age=52,
            boss=boss,
            salary=100)
boss <- new("Person",
            name="Mr. X",
            age=60)
# 9. Let john get a raise of 15 percent.
# 10. Print the new salary of john.
john@salary <- raise(john, percent=15)
print(john@salary)
# "Mr. X" now wants to send a secret message to john and he doesn't want other employees to find out.
# 11. Use the generic function secret to let "Mr. X" create an encrypted message with the shift you like. 
sms <- secret(boss, "You are the best employee I've ever had.")
print(sms)
# 12. Use the generic function secret to let john decrypt the encrypted message.
decrsms <- secret(john, sms)
print(decrsms)
# 13. Create an instance of a new Employee called suzan, let suzan try decryting the message. If your code is right, suzan's message should be even more decrypted because only john can decrypt the Message of "Mr. X".
suzan <- new("Employee",
           name= "Suzan",
           age=19,
           boss=boss,
           salary=150)
trydecr <- secret(suzan, sms)
print(trydecr)
### Part 4: Optional #### 
# Write your own test cases as you would like and use more of the methods you defined in the classes. 
# You can try changing the shift of an existing message using one of the class methods 
# Or you can try Decrypting the message of suzan. 
sms2 <- secret(boss, "Many of life’s failures are people who did not realize how close they were to success when they gave up.- Thomas A. Edison")
print(sms2)
sms3 <- secret(boss, sms2)
print(sms3)
sms3_decr <- secret(john, sms3)
print(sms3_decr)

test_case1 <- AnytextMessage("The shift of this text needs to be changed.", 6L)
shift1 <- test_case1$get_encr_msg()
print(paste("The current encrypted message is:", shift1))
print(paste("The current shift is", test_case1$get_shift()))
test_case1$change_shift(2L)
shift2 <- test_case1$get_encr_msg()
print(paste("Now, the message has become:", shift2))
print(paste("The new shift is", test_case1$get_shift()))

setGeneric(
  "secretdecrypter",
  function(object, message) {
    standardGeneric("secretdecrypter")
  }
)

setMethod(
  "secretdecrypter","Person",
  function(object, message) {
    m <- CeasarsDecoder(message)
    secretshift <- m$decrypt_message()[2]
    return (secretshift)
  }
)
test_case2 <- secret(boss, "Hello dear employees.")
print(test_case2)
suzanencr <- secret(suzan, test_case2)
print(suzanencr)
print(secretdecrypter(suzan, suzanencr))
setGeneric(
  "getdecrshift",
  function(object, message) {
    standardGeneric("getdecrshift")
  }
)

setMethod(
  "getdecrshift","Person",
  function(object, message) {
    m <- CeasarsDecoder(message)
    sh <- as.integer(m$decrypt_message()[1])
    return (paste("The encryption is", 26-sh))
  }
)
test_case3 <- secret(boss, "Find the shift of this message.")
print(test_case3)
suzanencr2 <- secret(suzan, test_case3)
print(suzanencr2)
print(getdecrshift(suzan, suzanencr2))

### Good Luck! ### 
### THE END ### 