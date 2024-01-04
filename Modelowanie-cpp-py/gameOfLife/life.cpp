#include<iostream>
#include<random>
#include<stdlib.h>
#include<chrono>
#include<thread>
#include<fstream>
#include<time.h>

//dla kompilacji
//g++ -O3 life.cpp

int sprawdzenie(int x, int suma)
{
	if (x == 1)
	{
		if (suma == 2 || suma == 3)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	else
	{
		if (suma == 3)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
}

bool yesOrNo(float probOfYes) //zwraca 1 z jakims prawdopodobienstwem
{
	return rand() % 100 < (probOfYes * 100);
}

int main( ) {
	std::cout << "start" << '\n';
	//rozmiary L = [10, 100, 200, 500, 1000] -> do zadania 3 wwybralem p0 = 0.3
	const int N = 500; //rozmiar //blad przy 1000 rozmiar, zakres? moze vectorem to zrobic?
	const int iter = 1000; //iteracje - czas Tmax
	const int sym = 100; //symulacje
	bool t[N][N]; //oryginal
	bool t2[N][N]; //temp
	//char t3[N][N]; //druk - *
	int check = 0;
	double counter = 0;
	//prawdopodobienstwa
	double proby[7] = { 0.1, 0.3, 0.6, 0.75, 0.8, 0.05, 0.95 };
	float probOfYes = proby[1];
	//zapisanie do pliku zywych
	std::ofstream myfile;
	myfile.open("GameOfLife-03-final-500.txt");
	//myfile << '\t' << N * N << '\n';

	std::cout << "iter" << '\n';

	std::srand(time(NULL));

	for (int i = 0; i < sym; i++)
	{
		std::cout << i << '\n';
		
		//tworzymy pierwsza tablice
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				int r = yesOrNo(probOfYes); //rand 0 to 1
				t[i][j] = r;
			}
		}

		//iteracje
		for (int x = 0; x < iter; x++)
		{
			//upload tablicy
			for (int i = 0; i < N; i++)
			{
				for (int j = 0; j < N; j++)
				{
					///////////////////////////////////////////////////////////////////////
					//gorna sciana
					//lewy rog
					if (i == 0 && j == 0)
					{
						check = t[i + 1][j] + t[i][j + 1] + t[i + 1][j + 1];
					}
					//prawy rog
					if (i == (N - 1) && j == 0)
					{
						check = t[i - 1][j] + t[i][j + 1] + t[i - 1][j + 1];
					}
					//reszta
					if (j == 0 && (i > 0 && i < (N - 1)))
					{
						check = t[i + 1][j] + t[i + 1][j + 1] + t[i - 1][j] + t[i][j + 1] + t[i - 1][j + 1];
					}
					///////////////////////////////////////////////////////////////////////
					//dolna scianka
					//lewy rog
					if (i == 0 && j == (N - 1))
					{
						check = t[i + 1][j] + t[i][j - 1] + t[i + 1][j - 1];
					}
					//prawy rog
					if (i == (N - 1) && j == (N - 1))
					{
						check = t[i - 1][j] + t[i][j - 1] + t[i - 1][j - 1];
					}
					//reszta
					if (j == (N - 1) && (i > 0 && i < (N - 1)))
					{
						check = t[i + 1][j] + t[i + 1][j - 1] + t[i - 1][j] + t[i][j - 1] + t[i - 1][j - 1];
					}
					///////////////////////////////////////////////////////////////////////
					//lewa scianka
					if ((j > 0 && j < (N - 1)) && i == 0)
					{
						check = t[i + 1][j] + t[i + 1][j - 1] + t[i + 1][j + 1] + t[i][j - 1] + t[i][j + 1];
					}
					///////////////////////////////////////////////////////////////////////
					//prawa scianka
					if ((j > 0 && j < (N - 1)) && i == (N - 1))
					{
						check = t[i - 1][j] + t[i - 1][j - 1] + t[i - 1][j + 1] + t[i][j - 1] + t[i][j + 1];
					}
					///////////////////////////////////////////////////////////////////////
					//srodek
					if ((j > 0 && j < (N - 1)) && (i > 0 && i < (N - 1)))
					{
						check = t[i - 1][j - 1] + t[i - 1][j] + t[i - 1][j + 1] + \
							t[i + 1][j - 1] + t[i + 1][j] + t[i + 1][j + 1] + \
							t[i][j - 1] + t[i][j] + t[i][j + 1];
					}

					//nadanie nowych wartosci
					t2[i][j] = sprawdzenie(t[i][j], check);
					//zliczenie zywych
					if (t[i][j] == 1)
					{
						counter += 1;
					}
				}
			}

			////przeniesienie do oryginalnej tablicy plus druk
			for (int i = 1; i < N - 1; i++)
			{
				for (int j = 1; j < N - 1; j++)
				{
					//przeniesienie do oryginalnej tablicy
					t[i][j] = t2[i][j];

					//druk
					/*
					if (t[i][j] == 1)
					{
						t3[i][j] = '*';
					}
					if (t[i][j] == 0)
					{
						t3[i][j] = '-';
					}
					*/
				}
			}
			//print
			/*
			system("CLS");
			for (int i = 1; i < N - 1; i++)
			{
				std::cout << '\n';
				for (int j = 1; j < N - 1; j++)
				{
					std::cout << t3[i][j];
				}
			}
			std::this_thread::sleep_for(std::chrono::milliseconds(100));
			*/

			//std::cout << counter << '\n';
			double ans = counter / (N * N);
			myfile << ans << '\n';
			counter = 0;
		}
	}
	
	myfile.close( );
	std::cout << "done" << '\n';

    //stan ustalony:
    //1. wiecej iteracji
	//2. srednia z max i min z okna czasowego (np. 10 iteracji) -> 80 - 90 iteracje

	//0.1 -> 0.0325
	//0.3 -> 0.04425
	//0.6 -> 0.051199999999999996
	//0.75 -> 0.052000000000000005
	//0.8 -> 0.05425
}