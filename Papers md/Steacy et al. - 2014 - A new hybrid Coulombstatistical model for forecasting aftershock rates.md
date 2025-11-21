# Steacy et al. - 2014 - A new hybrid Coulombstatistical model for forecasting aftershock rates

Geophysical Journal International

Geophys. J. Int. (2014) 196, 918–923
Advance Access publication 2013 November 11

doi: 10.1093/gji/ggt404

A new hybrid Coulomb/statistical model for forecasting
aftershock rates

Sandy Steacy,1 Matt Gerstenberger,2 Charles Williams,2 David Rhoades2
and Annemarie Christophersen2
1School of Environmental Sciences, University of Ulster, Cromore Road, Coleraine, BT52 1SA, Northern Ireland. E-mail: s.steacy@ulster.ac.uk
2GNS Science, 1 Fairway Drive, P.O. Box 30368, Lower Hutt, New Zealand

Accepted 2013 October 1. Received 2013 September 30; in original form 2013 July 28

S U M M A R Y
Forecasting the spatial and temporal distribution of aftershocks is of great importance to
earthquake scientists, civil protection authorities and the general public as these events cause
disproportionate damage and consternation relative to their size. At present, there are two
main approaches to such forecasts—purely statistical methods based on observations of the
initial portions of aftershock sequences and a physics-based approach based on Coulomb
stress changes caused by the main shock. Here we develop a new method which combines the
spatial constraints from the Coulomb model with the statistical power of the STEP (short-term
earthquake probability) approach. We test this pseudo prospectively and retrospectively on
the Canterbury sequence against the STEP model and a Coulomb rate–state method, using
data from the ﬁrst 10 d following each main event to forecast the rate of M ≥ 4 events in the
following 100 d. We ﬁnd that in retrospective tests the new model outperforms STEP for two
events in the sequence but this is not the case for pseudo-prospective tests. Further, the Coulomb
rate–state approach never performs better than STEP. Our results suggest that incorporating
the physical constraints from Coulomb stress changes can increase the forecasting power of
statistical models and clearly show the importance of good data quality if prospective forecasts
are to be implemented in practice.

Key words: Probabilistic forecasting; Earthquake interaction, forecasting, and prediction;
Statistical seismology.

y
g
o
o
m

l

s
i
e
S

I
J
G

1 I N T R O D U C T I O N

There are two main statistical approaches to aftershock forecast-
ing, the ETAS (epidemic-type aftershock sequence, e.g. Ogata
1988; Ogata & Zhuang 2006) and short-term earthquake proba-
bility (STEP; Gerstenberger et al. 2005) models. Both rely on two
fundamental observations in seismology, the Gutenberg–Richter re-
lation and the Omori Utsu law. In the ETAS model every earthquake
is a main shock with its own aftershock sequence and the rate of
earthquake occurrence depends on the background seismicity rate
and the productivity of each main shock in terms of triggering af-
tershocks (Ogata 1988).

The STEP model (Gerstenberger et al. 2005) is also based on
superimposed Omori sequences, where every earthquake is allowed
to generate its own aftershock sequence. A forecast is created us-
ing an ensemble of three different models of increasing complexity,
which are combined using weights calculated from the Akaike In-
formation Criterion (Burnham & Anderson 2002). Spatially, the
ensemble forecast is typically dominated by the most simple model
which is based on STEP parameters from the historical catalogue.

For this component of the ensemble forecast, a fault is estimated
from the observed aftershock distribution and the forecast rates are
isotropically smoothed away from the fault using a 1/r2 taper. Spa-
tial heterogeneity is then added to the forecast using parameters that
are estimated based on the ongoing sequence.

In contrast, the Coulomb method is a physics-based approach,
which calculates the static stress changes due to earthquake slip
in the nearby region. These stress changes have been shown by a
number of authors to inﬂuence the spatial distribution of subse-
quent events and, in particular, aftershocks tend to occur in areas
where the Coulomb stress has been increased due to main shock
rupture (see Steacy et al. 2005, for a review). Potential rate changes
due to Coulomb stress perturbations are generally computed
through a rate–state formulation based on laboratory friction models
(Dieterich 1994; Parsons et al. 2000; Toda et al. 2005). The key ex-
perimental observation is that friction is an acceleration to failure
process and hence, with the assumption of a uniform population
of future nucleation sites, the Dieterich formulation (1994) allows
computation of the expected rate of seismicity for a given stress
change and background rate.

918

C(cid:3) The Authors 2013. Published by Oxford University Press on behalf of The Royal Astronomical Society.

One limitation of the Coulomb rate–state approach is its depen-
dence on poorly deﬁned parameters such as background loading
rate, aftershock decay rate and a constitutive parameter (Hainzl
et al. 2010). Additionally, the forecast aftershock rate is strongly
dependent on the magnitude of the stress change at any location
(Dieterich 1994; Hainzl et al. 2009) and this, in turn, depends di-
rectly on knowledge of the detailed slip distribution of the causative
event (Steacy et al. 2004). However, it is quite common for several
very different slip models to be published after any particular event
and these can lead to very different forecasts (Hainzl et al. 2009).

Here we develop a new method for forecasting aftershock rates,
which combines the statistical approach of the STEP model with
the spatial constraints provided by the Coulomb stress changes.
We apply the new model to the Canterbury earthquake sequence
and test it against the New Zealand application of the STEP model
and an implementation of the Coulomb rate–state model (C-RS).
Since 2010, the Canterbury region has experienced four signiﬁcant
earthquakes that migrated from west to east—in order these are
the Mw = 7.1 Darﬁeld event of 2010 September 4, the Mw = 6.2
Christchurch earthquake of 2011 February 22, a further Mw = 6.0
event on 2011 June 13 and Mw = 5.8 and 5.9 events on 2011
December 23.

2 M E T H O D

We avoid the problems associated with accurate calculation of stress
change magnitudes by treating the stress ﬁeld as a Boolean and
modifying STEP forecasts based purely on the computed pattern of
positive/negative stress. Speciﬁcally, we run the STEP model as our
base but redistribute forecast rates so the 93 per cent of events are
expected to occur in positively stressed regions; this value comes
from our observations of the correlation between positive stress
and aftershocks in several California sequences (so in essence it’s a
generic parameter). We investigate two variations of this model, one
(STEPC1) in which we apply the STEP model within 5 km of the
fault zone but redistribute rates away from it; the other (STEPC2)
in which we apply the Coulomb-based redistribution everywhere.

We compute the Coulomb stress patterns by resolving the tenso-
rial stress perturbation onto 3-D optimally oriented planes at a depth
of 7.5 km assuming an effective coefﬁcient of friction of 0.4. We
use regional horizontal stress orientations of σ 1 = 115◦, σ 3 = 25◦
with σ 2 vertical (Sibson et al. 2011), and assume compressive stress
values of σ 1 = 10 MPa, σ 2 = 0.5 MPa and σ 3 = 0.1 MPa; the near
equal values of the latter are consistent with observations of both
strike-slip and reverse faulting in the region (Sibson et al. 2011).
The stress values are consistent with the literature (e.g. Toda et al.
2005) and have been used throughout this study without any attempt
at optimization. The calculations are done for an elastic half-space
and we assume that the Lame constants (λ and μ) are each equal to
3 × 104 MPa

The slip models for the pseudo-prospective tests (‘10 d’) were
provided to us by Caroline Holden (personal communication, 2012)
as she has a record of the dates on which each preliminary model
was computed. For the retrospective tests, we chose the six-fault
model of Beavan et al. (2012) for the Darﬁeld earthquake, for the
February event, we use the source model of Holden (2011) and
for the June and December earthquakes we use the source models
described in Holden & Beavan (2012).

In the Coulomb rate–state model, we calculate seismicity rate
changes using the method of Catalli et al. (2008) which computes
the reference shear stressing rate from the reference seismicity rate

Model for forecasting aftershock rates

919

and apply the Dieterich formulation (1994) to compute the response
of the seismicity rate to sudden stress steps. (See Supporting Infor-
mation for more details.) We compute the reference seismicity rate
using the Proximity to Past Earthquakes (PPE) smoothed seismicity
model as implemented by Rhoades & Evison (2004). The reference
model smooths the locations of earthquakes with magnitude M ≥
4.0 from 1964 January 1 to 2011 September 3 (just prior to the
Darﬁeld main shock) using an inverse power-law smoothing kernel
and weighting all earthquakes equally. All calculations and tests are
performed on a 0.05◦ × 0.05◦ grid.

3 R E S U LT S

We test the models by using the ﬁrst 10 d of data after each event
to forecast the rates of M ≥ 4 aftershocks in the subsequent 100 d.
We do this both retrospectively using currently available data and
pseudo-prospectively based on the data actually available at the
time. For the latter, we ensure that we only use slip models that
would have been available within the ﬁrst 10 d; for instance for
the Darﬁeld event this slip model was a single approximately E–
W striking fault plane with primarily right lateral displacement.
By contrast, a later more sophisticated model incorporating GPS
and InSAR data contained six faults—including two with primarily
thrust motion (Beavan et al. 2012). Note that this model is used in
the pseudo-prospective forecasts for the later events because it was
available in 2010 November, well within the learning periods for
the 2011 forecasts.

The pseudo-prospective forecasts following the Darﬁeld earth-
quake are shown in Fig. 1. The Coulomb pattern is clearly evident in
the STEPC models with areas of higher forecast rate corresponding
to regions of positive Coulomb stress, and lower rates in negative
stress locations. Both STEPC models have greater near fault forecast
rates than STEP as a result of the positive Coulomb stress adjacent
to the fault zone; the on-fault rates in STEPC2 are the highest of the
three models because of the superposition of the STEP 1/r2 taper
and the Coulomb-based rate redistribution.

The forecast rates from the Coulomb rate–state model are very
different from the STEP-derived approaches. The overall forecast
rate is generally less (Table 1) because the background rate is very
low as the Canterbury Plain experienced little seismicity prior to the
Darﬁeld event. Additionally, the large negative stress drops close
to the fault zone lead to some very low forecast rates, for instance
three M > 4 aftershocks occurred in locations where the forecast
rate is less than 10−14.

The dependence of the Coulomb stress pattern (and the forecast
rates) on the slip model is apparent from comparison with Fig. 2
where we plot the forecast rates for the retrospective models. Here
the northerly lobe of Coulomb stress is rotated to the east because the
six-fault slip model contains the NE-striking Charing Cross thrust
fault north of the main E–W fault plane. The total forecast rate for
the STEP models is slightly higher due to the greater number of
events in the retrospective catalogue used in the learning period.

The Coulomb rate–state model shows the greatest change with
much higher forecast rates in the northerly lobe of positive stress
and adjacent to the fault zone. The former results from higher stress
magnitudes in that region and the latter is due to an increased area
of positive stress due to the additional faults. With the retrospective
slip distribution the total forecast rate is 47.4 (quite close to the
observed value of 49), whereas for this pseudo-prospective model
the total rate was only 28.7. Note that both the pseudo-prospective
and retrospective STEP models signiﬁcantly overestimate the rate.

920

S. Steacy et al.

Figure 1. Forecast rates following the Darﬁeld earthquake for the four pseudo-prospective models. From left to right, top to bottom, these are STEPC1 (with
STEP on the fault zone), STEPC2 (applying the Coulomb ﬁlter everywhere), Coulomb rate–state and STEP. Open circles indicate the epicentres of the M ≥ 4
aftershocks that occurred in the 100-d testing period.

Table 1. Observed and forecast number of M ≥ 4 af-
tershocks in each 100-d testing period. The abbreviation
‘pp’ indicates results for pseudo-prospective tests and ‘r’
stands for retrospective. The forecast number of events
for the STEPC models is the same as for STEP since the
Coulomb ﬁlter simply redistributes rate.

Darﬁeld

February

June

December

Observed
STEP_pp
C-RS_pp
STEP_r
C-RS_r

49
76.9
28.7
78.4
47.4

30
22.7
16.4
22.7
21.4

24
22
16.6
27
18.8

27
15.6
16.5
20.8
16.0

(The pseudo-prospective and retrospective forecasts for the later
sequences are shown in Figs S1–S6.)

In Table 2, we compare the STEPC and Coulomb rate–state mod-
els to STEP for each earthquake and input data set using a t-test
which measures the signiﬁcance of the information gain per earth-
quake (IGPE) of one model over another (Rhoades et al. 2011).
The IGPE is the increase in the log-likelihood divided by the num-
ber of earthquakes; a 95 per cent conﬁdence interval for the IGPE
that does not include zero indicates a signiﬁcant difference in the
information value of the two models.

Our ﬁrst observation is that the pseudo-prospective Coulomb
rate–state models always perform signiﬁcantly worse than STEP
and its derivatives, although the model performance compared to
STEP improves with later events. The same pattern is observed for
the retrospective tests, with the model performance for the ﬁrst three
events worse than STEP but with improvement to equivalent within
conﬁdence limits for the December test.

The comparison between the STEPC models and STEP is more
complicated. For the pseudo-prospective tests, the new models per-
form worse than STEP for the Darﬁeld and December sequences
and the same within conﬁdence limits for the February and June
ones. However, with the more developed slip models, both perform
equally well as STEP for the September and February sequences
and better for December. For the June sequence, both models per-
form better than STEP but only STEPC1 (where STEP is applied
along the fault zone) does so when conﬁdence limits are considered.
[Note that we also computed a modiﬁed version of the s-test (Zechar
et al. 2010), using a log-likelihood function, which ignores the dis-
cretization of space into cells (Rhoades et al. 2011), and found that
all models, including C-RS, are consistent with the data.]

4 D I S C U S S I O N A N D C O N C L U S I O N S

The results are strongly dependent on the accuracy of the slip model
and this is clear from comparisons between the different retrospec-
tive forecasts as well as between pseudo-prospective and retrospec-
tive ones. In the case of Darﬁeld, for instance, the original slip
distribution (a single E–W plane) is very different from the one
used subsequently (six faults, three with NE/SW orientations) and
this may explain why all the Coulomb models perform worse than
STEP which is independent of externally derived slip distributions.
The improvement in the retrospective tests is likely due to the use
of a more accurate slip model, however the better performance of
the STEP model may suggest that the six-fault model does not fully
capture the complexity of the Darﬁeld rupture.

We test this retrospectively using two other sets of slip models,
one obtained by Atzori et al. (2012) who modelled the Darﬁeld,

Model for forecasting aftershock rates

921

Figure 2. Forecast rates following the Darﬁeld earthquake for the four retrospective models. From left to right, top to bottom, these are STEPC1, STEPC2,
Coulomb rate–state and STEP. Open circles indicate the epicentres of the M ≥ 4 aftershocks that occurred in the 100-d testing period.

Table 2. Results of the t-tests for information gain per earthquake (IGPE) for the various models
and input data sets. The set on the left is for the pseudo-prospective tests whereas the one on the
right is for the retrospective ones. Each model is compared to the STEP model (with the same input
data); negative values with conﬁdence limits less than the IGPE (shown in red) indicate models
that perform better than STEP whereas positive values with conﬁdence limits less than the IGPE
(blue) indicate models that do worse. Values that, within conﬁdence limits, range from negative to
positive are shown in green and indicate that within error the models perform as well as STEP;
bold type indicates those for which the IGPE is better than for STEP.

Christchurch, and June events and found that the Darﬁeld earth-
quake involved eight rupture planes, the Christchurch event two
and the June earthquake one; and the other from Elliott et al. (2012)
who modelled the Darﬁeld and Christchurch events and also found
eight and two rupture planes, respectively. The results are shown
in Table 3, the majority of these Coulomb-based models perform
better with respect to STEP than those derived from the six-fault
Darﬁeld slip model of Beavan et al. (2012). This suggests that the

slip models with eight rupture planes may better describe the com-
plex Darﬁeld rupture; this is in line with observations by Steacy
et al. (2013) that a greater percentage of aftershocks are consistent
with Coulomb triggering for stress maps computed using these slip
models compared to the one of Beavan et al. (2012).

The differences between the initial and ﬁnal forecasts of the
Coulomb-based models for the February earthquake are much less,
probably because the same slip model is used for Darﬁeld and the

922

S. Steacy et al.

Table 3. Results of the t-tests for information gain per earthquake (IGPE) for retrospective tests using the
slip models developed by Atzori et al. (2012) (Atz) and Elliott et al. (2012) (Ell). The colour coding is the
same as in Table 2 and there are no June results for Elliott et al. because the authors did not model the slip
in that earthquake.

difference between the slip models used for the February event is
relatively small. However, we note that both STEPC models perform
better than STEP in retrospective tests for forecasts built on the
slip models of Atzori et al. (2012). By contrast, the initial slip
model for June contained one fault plane whereas the one used
in the retrospective forecast has two; this may explain the larger
differences between the forecasts and also the poorer performance
for June compared to February of all the Coulomb-based models
in the pseudo-prospective tests. The effect of the slip model on the
results is strongest for the Coulomb rate–state model because the
forecasts depend on the magnitude of the stress change, not just the
sign. In addition, the STEP-derived models have an advantage over
the Coulomb rate–state one as they include seismicity information
from the learning periods which is not considered in C-RS.

that

Our results suggest

including spatial constraints from
Coulomb stress changes can increase forecasting power when good
data are available. This is consistent with the one prior study of a
hybrid model in which Bach & Hainzl (2012) retrospectively tested
a combined Coulomb/ETAS model for three California earthquakes
and found that the addition of the Coulomb information improved
forecasts of off-fault aftershock locations.

Additionally, our results suggest that these hybrid models which
combine stress patterns with statistical techniques may be more
appropriate than those based on the Coulomb rate–state method.
We believe that this is the ﬁrst (even pseudo) prospective test of
the Coulomb rate–state model and the results are consistent with
work by Woessner et al. (2011) who compared a set of statistical
and Coulomb models in a forward looking retrospective test on the
Landers earthquake; the parameters could not be altered but the
Coulomb modellers had access to a slip model published 2 yr after
the event. They found that the statistical models generally performed
better than Coulomb rate–state; no hybrid models such as the ones
presented here were tested.

Finally we ﬁnd that good data quality is crucial, particularly the
robustness of the slip inversions, and we suggest that this must
be considered carefully before prospective forecasts are put in the
public domain.

A C K N O W L E D G E M E N T S

We thank two anonymous reviewers for constructive comments
which improved the manuscript, as well as the Editor, Jeannot
Trampert, for handling it efﬁciently. We also thank Caroline Holden
for providing us with unpublished slip distributions and colleagues

at GNS Science for data and support. We acknowledge the New
Zealand GeoNet project and its sponsors EQC and GNS Science
for providing earthquake data used in the study. This work received
ﬁnancial support from GNS Science, the Natural Environment Re-
search Council, the Leverhulme Trust and the EC FP7 program
(contract # 282862) as part of the Strategies and tools for Real-
Time Earthquake Risk Reduction (REAKT) project.

R E F E R E N C E S

Atzori, S., Tolomei, C., Antonioli, A., Merryman Boncori, J.P., Bannis-
ter, S., Trasatti, E., Pasquali, P. & Salvi, S., 2012. The 2010–2011
Canterbury, New Zealand, seismic sequence: multiple source analy-
sis from InSAR data and modeling, J. geophys. Res., 117, B08305,
doi:10.1029/2012JB009178.

Bach, C. & Hainzl, S., 2012. Improving empirical aftershock modeling
based on additional source information, J. geophys. Res., 117, B04312,
doi:10.1029/2011JB008901.

Beavan, J., Motagh, M., Fielding, E., Donnelly, N. & Collett, D., 2012. Fault
slip models of the 2010–2011 Canterbury, New Zealand, earthquakes
from geodetic data, and observations of post-seismic ground deformation,
N. Z. J. Geol. Geophys., 55, 207–221.

Burnham, K.P. & Anderson, D.R., 2002. Model Selection and Multi-
model Inference, A Practical Information-Theoretic Approach, Springer-
Verlag.

Catalli, F., Cocco, M., Console, R. & Chiaraluce, L., 2008. Modeling seis-
micity rate changes during the 1997 Umbria-Marche sequence (central
Italy) through a rate- and state-dependent model, J. geophys. Res., 113,
B11301, doi:10.1029/2007JB005356.

Dieterich, J.H., 1994. A constitutive law for rate of earthquake production
and its application to earthquake clustering, J. geophys. Res., 99, 2601–
2618.

Elliott, J.R., Nissen, E.K., England, P.C., Jackson, J.A., Lamb, S., Li,
Z., Oehlers, M. & Parsons, B., 2012. Slip in the 2010–2011 Can-
terbury earthquakes, New Zealand, J. geophys. Res., 117, B03401,
doi:10.1029/2011JB008868.

Gerstenberger, M.C., Wiemer, S., Jones, L.M. & Reasenberg, P.A., 2005.
Real-time forecasts of tomorrow’s earthquakes in California, Nature, 435,
328–331.

Hainzl, S., Enescu, B., Cocco, M., Woesnner, J., Catalli, F., Wang, R. & Roth,
F., 2009. Aftershock modeling based on uncertain stress calculations,
J. geophys. Res., 114, B05309, doi:10.1029/2008JB006011.

Hainzl, S., Steacy, S. & Marsan, D., 2010. Seismicity models based on
Coulomb stress calculations, CORSSA, 25, doi:10.5078/corssa-32035809.
Holden, C., 2011. Kinematic source model of the 22 February 2011 Mw 6.2
Christchurch earthquake using strong motion data, Seismol. Res. Lett, 82,
783–788.

Holden, C. & Beavan, J., 2012. Kinematic source studies of the ongoing
(2010–2011) sequence of recent large earthquakes in Canterbury 2012,
in the Proceedings of NZSEE Conference, Christchurch.

Ogata, Y., 1988. Statistical models for earthquake occurrences and residual

analysis for point processes, J. Am. Stat. Assoc., 83, 9–27.

Ogata, Y. & Zhuang, J., 2006. Space-time ETAS models and an improved

extension, Tectonophysics, 413, 13–23.

Parsons, T., Toda, S., Stein, R.S., Barka, A. & Dieterich, J.H., 2000. Height-
ened odds of large earthquakes near Istanbul: an interaction-based prob-
ability calculation, Science, 288, 661–665.

Rhoades, D.A. & Evison, F.F., 2004. Long-range earthquake forecasting with
every earthquake a precursor according to scale, Pure appl. Geophys., 161,
47–72.

Rhoades, D., Schorlemmer, D., Gerstenberger, M., Christophersen, A.,
Zechar, J. & Imoto, M., 2011. Efﬁcient testing of earthquake forecast-
ing models, Acta Geophys., 59, 728–747.

Sibson, R.H., Ghisetti, F.C. & Ristau, J., 2011. Stress control of an evolving
strike-slip fault system during the 2010–2011 Canterbury, New Zealand,
earthquake sequence, Seismol. Res. Lett., 82, 824–832.

Steacy, S., Marsan, D., Nalbant, S.S. & McCloskey, J., 2004. Sensitivity of
static stress calculations to the earthquake slip distribution, J. geophys.
Res., 109, B04303, doi:10.1029/2002JB002365.

Steacy, S., Gomberg, J. & Cocco, M., 2005. Introduction to special section:
stress transfer, earthquake triggering, and time-dependent seismic hazard,
J. geophys. Res., 110, B05S01, doi:10.1029/2005JB003692.

Steacy, S., Jimenez, A. & Holden, C., 2013. Stress triggering and the Can-
terbury earthquake sequence, Geophys. J. Int., doi:10.1093/gji/ggt380.
Toda, S., Stein, R.S., Richards-Dinger, K. & Bozkurt, S., 2005. Fore-
casting the evolution of seismicity in southern California: animations
built on earthquake stress transfer, J. geophys. Res., 110, B05S16,
doi:10.1029/2004JB003415.

Woessner, J. et al., 2011. A retrospective comparative forecast

test
on the 1992 Landers sequence, J. geophys. Res., 116, B05305,
doi:10.1029/2010JB007846.

Zechar, J., Gerstenberger, M. & Rhoades, D., 2010. Likelihood-based tests
for evaluating space-rate-magnitude earthquake forecasts, Bull. seism.
Soc. Am., 100, 1184–1195.

Model for forecasting aftershock rates

923

S U P P O RT I N G I N F O R M AT I O N

Additional Supporting Information may be found in the online ver-
sion of this paper:

Figure S1: Pseudo prospective forecast rates for aftershocks fol-
lowing the February earthquake. As previously, top to bottom, left
to right, the models are STEPC1, STEPC2, C-RS, and STEP.
Figure S2: Retrospective forecast rates for aftershocks following
the February earthquake. As previously, top to bottom, left to right,
the models are STEPC1, STEPC2, C-RS, and STEP.
Figure S3: Pseudo prospective forecast rates for aftershocks fol-
lowing the June earthquake. As previously, top to bottom, left to
right, the models are STEPC1, STEPC2, C-RS, and STEP.
Figure S4: Retrospective forecast rates for aftershocks following
the June earthquake. As previously, top to bottom, left to right, the
models are STEPC1, STEPC2, C-RS, and STEP.
Figure S5: Pseudo prospective forecast rates for aftershocks fol-
lowing the December earthquake. As previously, top to bottom, left
to right, the models are STEPC1, STEPC2, C-RS, and STEP.
Figure S6: Retrospective forecast rates for aftershocks following
the December earthquake. As previously, top to bottom, left to right,
the models are STEPC1, STEPC2, C-RS, and STEP.
Table S1. Values used in computing reference shear stress rate from
reference seismicity rate.
Table S2. Frictional parameters used for Coulomb rate-state models.
(http://gji.oxfordjournals.org/lookup/suppl/doi:10.1093/gji/ggt404
/-/DC1)

Please note: Oxford University Press is not responsible for the con-
tent or functionality of any supporting materials supplied by the
authors. Any queries (other than missing material) should be di-
rected to the corresponding author for the article.
