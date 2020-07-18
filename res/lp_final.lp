// Author: Hung Le
// This code is a supporting material for my paper titled "A better bound on the largest indcued forests in triangle-free planar graph". 
// To compile and run the code, one should download and install lp_solve package version 5.5 at http://lpsolve.sourceforge.net/5.5/index.htm. 
// This code is supposed to run on Window 10. 
max: a- 2 b;
a >= 0;
a <= 1;
b >=0;
c >= 0;
d >= 0;
1 - a+ b -c >= 0;
1 - a+ b -d >= 0;
5 b - a >= 0;			//	exclude 5^+-vertex
5 + c + 12 b - 8 a >= 0;	//	exclude Q_3
4 + d + 8 b - 6 a >= 0;	//	exclude T_3
5 + 13 b - 8 a >= 0;	//	exclude Q^1_3
5 + 13 b - 8 a + c - d >= 0;	//	exclude Q^1_3
4 + 9 b - 6 a - d >= 0;	//	exclude T^1
5-8 a + 14 b - d >= 0;//	exclude Q^2_3
5-8 a + 14 b - c >= 0;//	exclude Q^2_3
5-8 a + 15 b - c -d>= 0;//	exclude Q^3_3
3 - 5 a + 10 b  - c  >= 0; // exclude T^4_6
3 - 5 a + 10 b  - d  >= 0; // exclude T^4_6
3 - 4 a + 4 b >= 0;        // exclude 2-2

