print('building static site')

top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index = open('content/index.html')
about = open('content/about.html')
experience = open('content/experience.html')
music = open('content/musicpost.html')
schiller = open('content/schiller.html')

open('docs/index.html', 'a+').write(top)
open('docs/index.html', 'a+').write(index)
open('docs/index.html', 'a+').write(bottom)

open('docs/about.html', 'a+').write(top)
open('docs/about.html', 'a+').write(about)
open('docs/about.html', 'a+').write(bottom)

open('docs/experience.html', 'a+').write(top)
open('docs/experience.html', 'a+').write(experience)
open('docs/experience.html', 'a+').write(bottom)

open('docs/musicpost.html', 'a+').write(top)
open('docs/musicpost.html', 'a+').write(music)
open('docs/musicpost.html', 'a+').write(bottom)

open('docs/schiller.html', 'a+').write(top)
open('docs/schiller.html', 'a+').write(schiller)
open('docs/schiller.html', 'a+').write(bottom)


