"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
Usage: 
"""
import logging
data = []
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20


#LECTURE SECTION 1
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log', 
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
try:
      file = open('module_4_data.txt')
      data = file.readlines()
      1/0
      file.close()
      print("File Closed")
except FileNotFoundError as e:
      logging.error("File does not exist")
except ZeroDivisionError as e:
      logging.error("ZeroDivisionError Exception: %s", e)
except Exception as e:
      logging.error("General Exception", e)
finally:
      if file is not None:
            file.close()
            logging.info("File Closed")

#LECTURE SECTION 2
try:
      if len(data) == 0:
            raise Exception("No data exist.")
      else:
            for record in data:
                  items = record.split(',')
                  title = items[0]
                  name = items[1]
                  salary = float(items[2])
                  
                  #LECTURE SECTION 3
                  #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
                  if salary > HIGH_SALARY:
                        logging.warning(f" {name}'s salary {salary} "
                                        + f" is currently above"
                                        + f" the recommended maximum"
                                        + f" is currently above"
                                        + f" the recommneded maximum"
                                        + f"{HIGH_SALARY}.")
                        
                  if salary * (1 + RECOMMENDED_INCREASE) > HIGH_SALARY:
                        logging.warning(f"{name}'s salary {salary} will be "
                                        + f" of {HIGH_SALARY}"
                                        + f" with the planned"
                                        + f"{RECOMMENDED_INCREASE} increase.")
                        
                  salary *= (1 + RECOMMENDED_INCREASE)
                  new_data.append([title,name,salary])
except Exception as e:
      logging.error("General Exception - Lecture 2", e)




#LECTURE SECTION 4
try:
      file = open('updated_salaries.txt', 'w')
      for record in new_data:
            row = ""
            for index, item in enumerate(record):
                  row += str(item)
                  if index < len(record) - 1:
                        row += (",")
            row += '\n'
            file.write(row)
except:
      logging.error("Exception writing data.")
finally:
      file.write("END OF FILE.")
      file.close()

#LECTURE SECTION 5
logging.debug('Debug level message.')
logging.info('Info level message.')
logging.warning('Warning level message.')
logging.error('Error level message.')
logging.critical('Critical level message.')
print("End of Program")

