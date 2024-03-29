# Image comression with DTC

Undergraduate project of the course [Methods of Scientific Computation](https://elearning.unimib.it/course/info.php?id=44604#en) (MSc in Computer Science at [University of Study in Milan-Bicocca](https://en.unimib.it/)).

The purpose of this project is to implement and use DCT2 in an open source environment on gray tone images, tests are then made to verify the correctness of the implementation, and a graphical interface is made to easily test the effects of DCT2 on images.

Is possible to read more details about the results obtained in the [Report(IT version)](Report%20-%20IT.pdf).

## Table of contents

- [Image comression with DTC](#image-comression-with-dtc)
  - [Table of contents](#table-of-contents)
  - [File description](#file-description)
  - [Contributors](#contributors)
  - [License](#license)

## File description

- `README.md`
  - Technical description of the project
- `utils.py`
  - Definition of functions useful for apllication
- `interface.py`
  - Executable file where the application interface is constriuted that calls the due methods for image compression
- `DCT.py`
  - Implication file of the custom library on the DCT
- `testTimeDCT.py`
  - Check that the times should be proportional to $O(N^3)$ for the homemade DCT2 and to $O(N^2\log (N))$ for the obtained fast version made from an already made library(`cv2`)
  - The tests were done on matrices containing random numbers from 0 to 255 of the following size $\left[\begin{matrix}320\times320&640\times640&1280\times1280&2560\times2560&5120\times5120\end{matrix}\right]$
- `verifyDCT.py`
  - Dummy tests to verify correctness for both one-dimensional and two-dimensional DCT, performed checks on inverse DCT as well

## Contributors

- [Davide Grandesso](https://github.com/dadegrande99/)
- [Fabio Marini](https://github.com/fabbio00/)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) - see the [LICENSE](LICENSE) file for details.
