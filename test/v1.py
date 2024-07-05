#version 1
import genanki
from pathlib import Path

#Params
deck_name = 'Country Capitals'
deck_id = 2059400110
model_id = 1600301350
model_name = 'Basic'
output_name = deck_name + '.apkg'
output_path = Path('decks') / output_name

my_model = genanki.Model(
  model_id,
  'Basic',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },],
   css ='''
    .card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
    '''
  )

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires'])


my_deck = genanki.Deck(
  2059400110,
  deck_name)

my_deck.add_note(my_note)


#Media
# my_package = genanki.Package(my_deck)
# my_package.media_files = ['sound.mp3', 'images/image.jpg']


genanki.Package(my_deck).write_to_file(output_path)
