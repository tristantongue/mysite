print('building static site')

top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index = open('content/index.html').read()
about = open('content/about.html').read()
experience = open('content/experience.html').read()
music = open('content/musicpost.html').read()
schiller = open('content/schiller.html').read()

open('docs/index.html', 'w').write(top)
open('docs/index.html', 'a+').write(index)
open('docs/index.html', 'a+').write(bottom)

open('docs/about.html', 'w').write(top)
open('docs/about.html', 'a+').write(about)
open('docs/about.html', 'a+').write(bottom)

open('docs/experience.html', 'w').write(top)
open('docs/experience.html', 'a+').write(experience)
open('docs/experience.html', 'a+').write(bottom)

open('docs/musicpost.html', 'w').write(top)
open('docs/musicpost.html', 'a+').write(music)
open('docs/musicpost.html', 'a+').write(bottom)

open('docs/schiller.html', 'w').write(top)
open('docs/schiller.html', 'a+').write(schiller)
open('docs/schiller.html', 'a+').write(bottom)


