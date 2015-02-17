%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% This MATLAB script is used to call compute_daisy and display_descriptor.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
function [dzy] = callDaisy(image, x, y, r)

%%

load('../Tools/Daisy/compute_daisy.m');
load('../Tools/Daisy/display_descriptor.m');

frame = imread(image);

