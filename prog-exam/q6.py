email = "john.doe@unec.edu.az"

def find_company(email):
  start = email.find("@")
  if start == -1:
    return "email is not correct"
  
  end = email.find(".", start)
  if end == -1:
    return "email is not correct"

  return email[start+1:end] 

print(find_company(email))
