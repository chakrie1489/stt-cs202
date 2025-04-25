using System;
using System.Threading.Tasks;
using static Move;

int wins = 0;
int draws = 0;
int losses = 0;
while (true)
{
	Console.Clear();
	Console.WriteLine("Rock, Paper, Scissors");
	Console.WriteLine();

	Move playerMove;
	while (true)
	{
		Console.Write("Choose [r]ock, [p]aper, [s]cissors, or [e]xit: ");
		Task<string?> inputTask = Task.Run(() => Console.ReadLine());
		if (!inputTask.Wait(TimeSpan.FromSeconds(10)))
		{
			Console.WriteLine("\nNo input received within 10 seconds. Exiting game...");
			return; // Exit the game if no input is received within the timeout period
		}
		string? input = inputTask.Result?.Trim().ToLower();

		if (input is "r" or "rock") { playerMove = Rock; break; }
		else if (input is "p" or "paper") { playerMove = Paper; break; }
		else if (input is "s" or "scissors") { playerMove = Scissors; break; }
		else if (input is "e" or "exit") { Console.Clear(); return; }
		else Console.WriteLine("Invalid Input. Try Again...");
	}
	Move computerMove = (Move)Random.Shared.Next(3); // Bug fixed 
	Console.WriteLine($"The computer chose {computerMove}.");
	switch (playerMove, computerMove)
	{
		case (Rock, Paper) or (Paper, Scissors) or (Scissors, Rock):
			Console.WriteLine("You lose.");
			losses++;
			break;
		case (Rock, Scissors) or (Paper, Rock) or (Scissors, Paper):
			Console.WriteLine("You win.");
			wins++;
			break;
		default:
			Console.WriteLine("This game was a draw.");
			draws++;
			break;
	}
	Console.WriteLine($"Score: {wins} wins, {losses} losses, {draws} draws");
	Console.WriteLine("Press Enter To Continue...");
	Console.ReadLine();
}

enum Move
{
	Rock = 0,
	Paper = 1,
	Scissors = 2,
}
