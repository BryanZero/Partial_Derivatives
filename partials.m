function partials = partials(expression, variables, varargin)
% Calculates partial derivatives of a given mathematical expression with respect to one or more variables.
% Use example:
%
% syms z y x
% z = x^2 + y^2*x
% partials = partials(z,{x y})
%
% You can use subs(partials.quad.eq,{variables},{values}) to evaluate the
% expression and recieve an answer.

partials = struct();

partials.Equation.eq = expression;
partials.Equation.latex = latex(expression);


tmp = 0;

for k=variables
   partial = diff(expression,k);
   partials.(string(k)).eq = partial;
   partials.(string(k)).latex = latex(partial);
   a = sym(strcat('sigma_',string(k)));
   tmp = partial^2*a^2 + tmp;
end

%Quadrature is given by

quad = sqrt(tmp);
quads = simplify(quad,'IgnoreAnalyticConstraints',1);
partials.quad.eq = quads;
partials.quad.latex = latex(quads);

%nInputs = numel(varargin);

% if nInputs > 0
%     partials.quad.eval = subs(quad, variables, varargin(1));
% end

