
        let rps = ['Rock', 'Paper', 'Scissors'];
        function random_element(array) {
	        let random_index = Math.floor(Math.random()*array.length);
	        return array[random_index];
        }

        document.querySelector('#bt_throw').onclick = play;



        function play() {
            const choices = document.getElementsByName("choice");
            console.log('help');
            let user_choice;
            for (let i = 0; i < choices.length; i++) {
                if (choices[i].checked)
                    user_choice = choices[i].value;
            }
            let computer_choice = random_element(rps);

            document.querySelector('#cpu_throw').innerText = computer_choice;
            document.querySelector('#player_throw').innerText = user_choice;

            if (computer_choice === user_choice) {
                document.querySelector('#outcome').innerText = 'Tie!';
            }
            else if (computer_choice === 'Rock' && user_choice === 'Scissors' || computer_choice === 'Paper' && user_choice === 'Rock' || computer_choice === 'Scissors' && user_choice === 'Paper') {
                document.querySelector('#outcome').innerText = 'Cpu wins!';
            }
            else {
                document.querySelector('#outcome').innerText = 'Player wins!';
            }
        }
