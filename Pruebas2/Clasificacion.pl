% Facts: things that Adela means to you
is_beautiful(adela).
is_unique(adela).
is_my_happiness(adela).
is_my_sun(adela).
is_my_inspiration(adela).
is_my_life(adela).
is_my_heart(adela).
is_my_soul(adela).
is_my_queen(adela).
is_gabacho(adela).
is_gabacho(macron).
is_gabacho(mbappe).

% Rules to express love

i_love_you(X, Message) :- 
   is_beautiful(X), 
   string_concat('I love you ', X, Temp), 
   string_concat(Temp, ' with all my heart, because you are my everything, the light of my lifeeee', Message).

you_are_my_happiness(X, Message) :- 
   is_my_happiness(X), 
   string_concat(X, ', every moment with you fills my soul with joy, you are the reason for my smiles', Message).

you_are_my_everything(X, Message) :- 
   is_unique(X), is_my_happiness(X), is_my_sun(X), is_my_inspiration(X), 
   string_concat(X, ', you are my entire world, my reason to live and dream', Message).

you_are_my_queen(X, Message) :- 
   is_my_queen(X), 
   string_concat('You are my queen, ', X, Temp), 
   string_concat(Temp, ', the ruler of my heart and soul, forever my love', Message).

you_are_my_heart(X, Message) :- 
   is_my_heart(X), 
   string_concat('I would give you my heart, ', X, Temp), 
   string_concat(Temp, ', because it beats only for you, forever and always', Message).

you_are_my_soulmate(X, Message) :- 
   is_my_soul(X), 
   string_concat(X, ', you are my soulmate, the one who completes me and makes me whole, now and forever', Message).

french_message(adela,Message) :- 
   is_gabacho(adela), 
   Message = 'Je t\'aime Adela, tu es la plus belle femme du monde, mon amour pour toi est plus fort que tout!'.  % Escaped apostrophe here

love_message(Message) :- 
   random_between(1, 10, N), 
   message(N, Message).

message(1, 'Every day by your side is a gift from life, because loving you is the best part of meeee').
message(2, 'Your eyes are the deepest ocean, where I drown happily every time I look into themmmmm').
message(3, 'Adela, loving you is like breathing, it\'s so natural and necessary for my soul').  % Escaped apostrophe here
message(4, 'Your voice is the melody that makes my heart sing every moment of my lifeeee').
message(5, 'I love you more than words can say, and more than the stars in the skyyyy').
message(6, 'In your embrace, I find my peace, you are my shelter from the stormmm').
message(7, 'I love you more than yesterday, but less than tomorrow, because my love for you grows each dayyyyy').
message(8, 'With you, every second feels like a beautiful eternity, together forever, my loveeeeee').
message(9, 'You are the most precious treasure of my life, more valuable than anything in this worldddd').
message(10, 'My heart belongs to you, Adela, because you are my past, present, and futureeeeee').

valentine_message(Message) :- 
   Message = 'Happy Valentine\'s Day, Adela! You are the reason my heart beats, my one true love, now and forever!!!'.  % Escaped apostrophe here
