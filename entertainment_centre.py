import media
import fresh_tomatoes

snatch = media.Movie("Snatch",
	"Illegal boxing promoter Turkish (Jason Statham) convinces gangster Brick Top (Alan Ford) to offer bets on bare-knuckle boxer Mickey (Brad Pitt) at his bookie business. When Mickey does not throw his first fight as agreed, an infuriated Brick Top demands another match. Meanwhile, gangster Frankie Four Fingers (Benicio Del Toro) comes to place a bet for a friend with Brick Top's bookies, as multiple criminals converge on a stolen diamond that Frankie has come to London to sell.",
	"http://t3.gstatic.com/images?q=tbn:ANd9GcT99CTVO4nyRGm0UcmDLo7Gv_InmxIoJkVlCDB1pdHho_vYjpig",
	"https://youtu.be/ni4tEtuTccc")
						
man_on_fire = media.Movie("Man on Fire",
	"In a Mexico City wracked by a recent wave of kidnappings, ex-CIA operative John Creasy (Denzel Washington) reluctantly accepts a job as a bodyguard for 9-year-old Lupita (Dakota Fanning), the daughter of wealthy businessman Samuel Ramos (Marc Anthony). Just as Creasy begins to develop a fondness for the young girl, a bloodthirsty gunman (Jesús Ochoa) kidnaps her. Now, Creasy must pick off a succession of corrupt cops and criminals to reach his ultimate object of vengeance.",
	"http://www.gstatic.com/tv/thumb/movieposters/34417/p34417_p_v7_aa.jpg",
	"https://youtu.be/g4kLizDXLY0")
						  
training_day = media.Movie("Training Day",
	"Police drama about a veteran officer who escorts a rookie on his first day with the LAPD's tough inner-city narcotics unit. Training Day is a blistering action drama that asks the audience to decide what is necessary, what is heroic and what crosses the line in the harrowing gray zone of fighting urban crime. Does law-abiding law enforcement come at the expense of justice and public safety? If so, do we demand safe streets at any cost?",
	"http://www.gstatic.com/tv/thumb/movieposters/28363/p28363_p_v7_aa.jpg",
	"https://youtu.be/DXPJqRtkDP0")
						   
interstellar = media.Movie("Interstellar",
	"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
	"https://youtu.be/2LqzF5WauAw")
						   
the_martian = media.Movie("The Martian",
	"When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
	"https://youtu.be/ej3ioOneTy8")

beeba_boys = media.Movie("Beeba Boys",
	"Jeet Johar, a guarded, ruthless gangster within the very real criminal underground populated by second- and third-generation Indian immigants on Canada’s west coast. As Jeet competes with rival gangs for an increasingly shrinking turf, the single father and dutiful son is forced to violently demand respect, ensuring the Beeba Boys’ continued survival in Vancouver.",
	"http://mediafiles.cineplex.com/Blog/ComicCon/CC2015/BEEBABOYS_OneSheet.jpg",
	"https://youtu.be/WDJxWig0hCk")
						  
movies = [snatch, man_on_fire, training_day, interstellar, the_martian, beeba_boys]
fresh_tomatoes.open_movies_page(movies)