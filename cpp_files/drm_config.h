#ifndef DRM_CONFIG_H_
#define DRM_CONFIG_H_

#include "drm_tables.h"
#include "drm_global_constants.h"
#include <iostream>

/* class holding the initial (user defined) parameters from which the others are derived */
class config
{
	unsigned short d_RM; // robustness mode (0-4 correspond to A-E)
	unsigned short d_SO; // spectrum occupancy (0-5)
	bool d_UEP; // 0: EEP, 1: UEP (only MSC, SDC & FAC are restricted to EEP and SM)
	unsigned int d_n_bytes_A; // number of higher protected bytes (if UEP is used)
	bool d_text; // 0: text message not used, 1: text message used
	unsigned short d_msc_mapping; // 0: 4-QAM SM (only RM E), 1: 16-QAM SM, 2: 64-QAM SM, 3: 64-QAM HMsym, 4: 64-QAM HMmix
	unsigned short d_msc_prot_level_1; // Protection level for higher protected part (if UEP is used)
	unsigned short d_msc_prot_level_2; // Protection level for lower protected part (or if EEP is used)
	unsigned short d_sdc_mapping; // 1: 4-QAM, 0: 16-QAM
	unsigned short d_sdc_prot_level; // (only for RM E) 0: 0.5, 1: 0.25
	bool d_long_interl; // 0: short interleaving, 1: long interleaving

	tables* d_ptables; // pointer to tables needed for init

public:
	/* accessor methods */
	unsigned short RM();
	unsigned short SO();
	bool UEP();
	unsigned int n_bytes_A(); // TODO: extend check_args()
	bool text();
	unsigned short msc_mapping();
	unsigned short msc_prot_level_1(); // TODO: extend check_args()
	unsigned short msc_prot_level_2();
	unsigned short sdc_mapping();
	unsigned short sdc_prot_level();
	bool long_interl();

	config();
	~config(){};

	void init(tables* ptr_tables); // set member variables
	bool check_arguments(); // some range and plausability checks
};

#endif