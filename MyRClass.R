#### HELPER CODE #######
setClass("Person", slots=c(name = "character", age = "numeric"))
### END HELPER CODE ###
library(reticulate)
source_python("myPythonClass.py")
# Part 1. 
# Your program is based on S4 objects.
# Consider that an employee is a person who has a salary and gets a raise from time to time.

# 1. Write an inherited class from the Person class, called Employee, who's attributes are boss (which is a Person object) and the salary (which is a numeric object).
setClass("Employee", slots = c(boss = "Person", salary="numeric"), contains="Person")
# 2. Write a Generic function called raise with the following arguments: An object and a percentage numeric variable.   
setGeneric(
  "raise",
  function(object, percent="numeric") {
    standardGeneric("raise")
  }
)
setMethod(
  "raise","Employee",
  function(object, percent=0) {
    return ((object@salary)+(object@salary*(percent/100)))
})

# 3. Write the Employee's specific method for the generic function raise which will take the object and percentage as an argument.
# For example if raise was called on an Employee object it should be used as follows:
# raise(john, percent=10) where john is an instance of the Employee object and percent is the raise percentage that will be applied on John's salary.

# Part 2.
# 4. Create a generic function called secret with th following arguments: The object and a message variable which will be a string. 

setGeneric(
  "secret",
  function(object, message) {
    standardGeneric("secret")
  }
)
setMethod(
  "secret","Person",
  function(object, message) {
    m <- AnytextMessage(message, 4L)
    secret <- m$get_encr_msg()
    return(secret)
  }
)
setMethod(
  "secret","Employee",
  function(object, message) {
    m <- CeasarsDecoder(message)
    sh <- as.integer(m$decrypt_message()[1])
    if(object@name=="John"){
      decr <- m$decrypt_message()[2]
      return (decr)
    }
    else{
      e <- AnytextMessage(message, as.integer(26-sh))
      encr <- e$get_encr_msg()
      return (encr)
    }
  }
)

# 5. Create a Person object's method for secret with the object and message arguments and let this method, encrypt a message using your Python encrypter. This function returns a string.
# 6. Create an Employee's object's method for secret with the object and message arguments and let this method, decrypt a message using your Python encrypter ONLY for Employees whos name is "John"! 
# If the employee's name is not "John", apply more encryption on top of the encrypted message. This function returns a string.


boss <- new("Person",
            name="Boss",
            age=30)
john <- new("Employee",
            name="John",
            age=25,
            boss=boss,
            salary=1000)
john@salary <- raise(john, percent=10)
john
ani <- new("Employee",
           name= "Ani",
           age=19,
           boss=boss,
           salary=1500)
print(secret(boss, "Hello"))
print(secret(john, "Jgnnq"))
print(secret(ani, "Jgnnq"))

