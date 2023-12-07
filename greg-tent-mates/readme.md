## Tent Mates 

In order to accomplish this task. I put on my hiking boots and took some mental notes about the situation.
In order for tme to enjoy the great outdoors I leave most unecessary technology behind and keep my arguments and fighting to a minimal.

My first approach was to open the files with **Pandas** I used `pd.read_csv` to quickly add the sizes of the tents and 
the campers and their personal preferences to a dataFrame. I then built custom methods to get each camper name 
and each tent size and append them to a datastructure for later iteration over them. 

the campers were placed into a list and the tents a dictionary to hold tent name and size or capacity as the corresponding value for the tent name key.

I then set a score value to represent the overall goal and then called `assignTents` this takes the tents dictionary and the campers list of names.
within the method it does what I consider the golden rule. assigns campers who respect each other. This is what I mean. It calculates the campers who won't fight each other based on their provided preference.
this is done by looking through each tent and adding the camper to the tent after checking if the other occupants in the tent aren't someone the current assigned camper isn't going to be angry or confrontational with.
I accomplish this by using pandas. within the `getDislikedCampers()` which takes a deep copy list of all the campers to compare. It checks to ensure that the campers are at a minimum level of 3 or below to establish a 
fighting criteria. My logic is that if that person is a 3 or below in preference they're not going to be happy campers if that person shows up in their tent. This is all done randomly with the `random.choice` function to allow some random behavior.

I choose from people who that camper doesn't like and ensure that they don't show up in the tent to being with. After this step an initial score is calculated with the starting arrangement.
by calling `calculateHappiness()` this method takes a dictonary list of camper names with their tent configuration. 

if the resulting score from the initial configuration isn't quite up to snuff. I then call `swapForHappierCampers()` with the campers and the current tentCamper Dictionary. this allows for the same process, 
but knowing that most of the campers will not be in positions to be too terribly unhappy with the occupants it swaps for random Happier person from the happier people within each tent. Doing the opposite of the current checking for dislikes expects it will swap
the campers to check each camper with a list of liked campers in order to maximize the happiness of each tent.

the process is run until the score is greater than 175.

I have had pretty good luck with this running through a few iterations and the randomizer solving the problems. 


**Running The Program**

ensure all the tent preferences and tent sizes are within the same directory of the project with the python files


installing the following package will be necessary to run the application

```shell
pip install pandas

# running the program
python tentMates.py
```

let me know if you have any issues running the program.

Greg