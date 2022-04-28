#create a file that reads in the top, middle and bottom html

top_html = open('./templates/top.html').read()

middle_html = open('./content/index.html').read()

bottom_html = open('./templates/bottom.html').read()

#create a file that combines the top middle and bottom html

combined_html = top_html + middle_html + bottom_html
#print(combined_html) to see if its working

#now takes combined html and writes file

open('./docs/index.html' , 'w+').write(combined_html)




#create a file that reads in the top, middle and bottom html

top_html = open('./templates/top.html').read()

middle_html = open('./content/education.html').read()

bottom_html = open('./templates/bottom.html').read()

#create a file that combines the top middle and bottom html

combined_html = top_html + middle_html + bottom_html
#print(combined_html) to see if its working

#now takes combined html and writes file

open('./docs/educaion.html' , 'w+').write(combined_html)




#create a file that reads in the top, middle and bottom html

top_html = open('./templates/top.html').read()

middle_html = open('./content/experience.html').read()

bottom_html = open('./templates/bottom.html').read()

#create a file that combines the top middle and bottom html

combined_html = top_html + middle_html + bottom_html
#print(combined_html) to see if its working

#now takes combined html and writes file

open('./docs/experience.html' , 'w+').write(combined_html)



#create a file that reads in the top, middle and bottom html

top_html = open('./templates/top.html').read()

middle_html = open('./content/skills.html').read()

bottom_html = open('./templates/bottom.html').read()

#create a file that combines the top middle and bottom html

combined_html = top_html + middle_html + bottom_html
#print(combined_html) to see if its working

#now takes combined html and writes file

open('./docs/skills.html' , 'w+').write(combined_html)