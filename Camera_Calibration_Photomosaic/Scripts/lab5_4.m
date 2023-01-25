A = imread('/Users/sumeghasinghania/Desktop/git/EECE5554/LAB5/Forsyth/PXL_20220330_172220782.MP.jpg');
% imshow(A)
I = im2gray(A);
imshow(I)
[y,x] = harris(I,1000,'tile',[2 2],'disp');

points = [x,y]

% imshow(I)