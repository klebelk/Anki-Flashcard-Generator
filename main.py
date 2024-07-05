# version 2
import genanki
import pandas as pd
from pathlib import Path


#Params
deck_name = 'Country Capitals'
deck_id = 2059400110
model_id = 1600301350
model_name = 'Basic'
output_name = deck_name + '.apkg'
output_path = Path('decks') / output_name

csv_path = 'samples\country-list.csv'
my_note = []
df = pd.read_csv(csv_path)
fields = df[['country', 'capital']].to_numpy()

my_model = genanki.Model(
  model_id,
  model_name,
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ],
  css ='''
    .card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
    '''
  )


my_deck = genanki.Deck(
    2059400110,
    deck_name)

for field in fields:
    # my_note[i] = genanki.Note(
    # model=my_model,
    # fields=fields[i])

    my_deck.add_note(genanki.Note(model=my_model,fields=field))


#Media
# my_package = genanki.Package(my_deck)
# my_package.media_files = ['sound.mp3', 'images/image.jpg']


genanki.Package(my_deck).write_to_file(output_path)
