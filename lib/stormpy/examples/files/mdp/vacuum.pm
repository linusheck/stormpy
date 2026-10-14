// Robot vacuum returning to its charging dock in a 5x4 living room.
//
//   y=3   S  S  .  .  D      S = stairs (robot falls)     D = charging dock
//   y=2   .  R  R  .  .      R = rug (more wheel slip)
//   y=1   .  R  R  F  .      F = under the sofa (robot gets stuck)
//   y=0   .  .  .  F  .
//        x=0 1  2  3  4
//
// Each move goes in the intended direction with probability 1-2*slip and
// slips sideways with probability slip each. The slip probability depends on
// the floor type. Walls block movement and trigger the bump sensor.
//
// Fully observable MDP variant used by examples/05-vacuum.py.

mdp

const int W = 4;
const int H = 3;
const double eTile = 0.05;
const double eRug  = 0.15;

formula stairs = y=H & x<=1;
formula sofa   = x=3 & y<=1;
formula rug    = (x=1 | x=2) & (y=1 | y=2);
formula dock   = x=W & y=H;
formula done   = stairs | sofa | dock;
formula active = started & !done;
formula slip   = rug ? eRug : eTile;

formula xl = max(x-1, 0);
formula xr = min(x+1, W);
formula yd = max(y-1, 0);
formula yu = min(y+1, H);


module vacuum
  x : [0..W] init 0;
  y : [0..H] init 0;
  bump : bool init false;
  started : bool init false;

  // The robot finishes cleaning at an unknown position along the bottom wall.
  [start] !started -> 1/3:(x'=0)&(y'=0)&(started'=true)
                    + 1/3:(x'=2)&(y'=0)&(started'=true)
                    + 1/3:(x'=4)&(y'=0)&(started'=true);

  [north] active -> (1-2*slip):(y'=yu)&(bump'=(y=H))
                  + slip:(x'=xl)&(bump'=(x=0))
                  + slip:(x'=xr)&(bump'=(x=W));
  [south] active -> (1-2*slip):(y'=yd)&(bump'=(y=0))
                  + slip:(x'=xl)&(bump'=(x=0))
                  + slip:(x'=xr)&(bump'=(x=W));
  [east]  active -> (1-2*slip):(x'=xr)&(bump'=(x=W))
                  + slip:(y'=yd)&(bump'=(y=0))
                  + slip:(y'=yu)&(bump'=(y=H));
  [west]  active -> (1-2*slip):(x'=xl)&(bump'=(x=0))
                  + slip:(y'=yd)&(bump'=(y=0))
                  + slip:(y'=yu)&(bump'=(y=H));
endmodule

label "docked" = dock;
label "failed" = stairs | sofa;
label "sofa" = sofa;
label "stairs" = stairs;
label "rug" = active & rug;
label "tile" = active & !rug;

rewards "steps"
  [north] true : 1;
  [south] true : 1;
  [east]  true : 1;
  [west]  true : 1;
endrewards

// Surface labels exclude the initial setup and absorbing terminal states.

// One reward per visit to an active rug state (not per movement action).
rewards "rug_visits"
  active & rug : 1;
endrewards
