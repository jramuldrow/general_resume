#create a file that reads in the top, middle and bottom html

def main():

# this for index.html
top_html = open('./templates/top.html').read()
middle_html = open('./content/index.html').read()
bottom_html = open('./templates/bottom.html').read()
combined_html = top_html + middle_html + bottom_html
open('./docs/index.html' , 'w+').write(combined_html)

#this is for the education page
top_html = open('./templates/top.html').read()
middle_html = open('./content/education.html').read()
bottom_html = open('./templates/bottom.html').read()
combined_html = top_html + middle_html + bottom_html
open('./docs/educaion.html' , 'w+').write(combined_html)

#this is for the expericene page
top_html = open('./templates/top.html').read()
middle_html = open('./content/experience.html').read()
bottom_html = open('./templates/bottom.html').read()
combined_html = top_html + middle_html + bottom_html
open('./docs/experience.html' , 'w+').write(combined_html)

#this is for the skills page
top_html = open('./templates/top.html').read()
middle_html = open('./content/skills.html').read()
bottom_html = open('./templates/bottom.html').read()
combined_html = top_html + middle_html + bottom_html
open('./docs/skills.html' , 'w+').write(combined_html)

main()

