def analize_mark(marks):
      return {
         "Max":max(marks),
         "Min":min(marks),
         "Average":sum(marks)/len(marks)
      }



marks=[56,87,34,67,76]
result=analize_mark(marks)
print(result)