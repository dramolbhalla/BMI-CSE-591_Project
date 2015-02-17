%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% This MATLAB script is used to call compute_daisy and display_descriptor.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
function callDaisy(image, x, y, r, compile)

%%
path(path, '../Tools/Daisy/');

if compile == 1
	mex '../Tools/Daisy/mex_compute_all_descriptors.cpp';
	mex '../Tools/Daisy/mex_compute_descriptor.cpp';
end

frame = imread(image);

dzy = compute_daisy(frame,r,3,8,8)
display_descriptor(dzy, y, x)
