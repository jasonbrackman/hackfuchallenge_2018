"""
You read the strange glowing poem.

	The house is a room.
	"They say nobody ever gets out
	No light can pierce its gloom
	Can't know what it's all about"

	The entrance is a door.
	"boarded shut for years."
	The exit is in the floor.
	"though it seldom appears."

	The field is southwest of the house.
	The house is west of the entrance.
	The angry dog is inside the house.
	"He values his independence."

	The entrance is west of the stream.
	West of the field is the pit of hell.
	A room can be a nightmare or a dream.
	"Especially if it's under a spell."

	The answers you seek are here.
	In the stanzas above is a map.
	"From east to west shall it appear.
	Zoom out to avoid the trap."

Right beneath the poem, in contrastingly rough-hewn and non-glowing letters, is a set of words with large spaces between them. It reads:

	hackfufirst      second      third      fourth      end
"""

""" Hell Field House Room Door """

import os
import challenge_00


def decrypt_message(passkey):
    infile_ = os.path.abspath('Challenges/Challenge 1/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 1/generated_content/solution.txt')
    print(os.path.isfile(infile_))
    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)


fourth = "pitofhell"
third = "field"
second = "house"
first = "stream"

key = f"hackfufirst{first}second{second}third{third}fourth{fourth}end"
decrypt_message(key)
