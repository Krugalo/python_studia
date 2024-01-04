#include<iostream>
#include<random>
#include<cstdlib>
#include<fstream>


int main( )
{
    //generator meersenne twister
    std::mt19937 generator(1234);
    std::uniform_real_distribution<double> dis(0.0, 1.0);

    //generator rand
    srand(1234);

    const int N = 100;

    std::ofstream f,fR, fMT;
    std::string filename, nameR, nameMT;
    filename = "spacer1.txt";
    nameR = "spacer1-daneR.txt";
    nameMT = "spacer1-daneMT.txt";
    f.open(filename);
    fR.open(nameR);
    fMT.open(nameMT);

    int arr[N] = {};
    int arrMT[N] = {};

    double d = 1.0 / N;

    double r, mt;
    double sumaR, sumaMT;

    for (int i = 0; i < 100'000; i++)
    {
        r = ((double) rand() / (RAND_MAX));
        mt = dis(generator);
        std::cout << r << " " << mt << '\n';
        
        for (int j = 0; j < N; j++)
        {
            if (r > (j*d) && r < (j*d+d))
            {
                arr[j] += 1;
            }

            if (mt > (j*d) && mt < (j*d+d))
            {
                arrMT[j] += 1;
            }
        }
        
        fR << r << '\n';
        fMT << mt << '\n';
    }

    for (int i = 0; i < N; i++)
    {
        std::cout << i << " " << arr[i] << " " << arrMT[i] << '\n';
        f << i*d << " " << arr[i] << " " << arrMT[i] << '\n';
    }

    f.close( );
}