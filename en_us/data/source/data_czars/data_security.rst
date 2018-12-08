.. _Data Security Guidelines:

#######################################
Data Security Guidelines for Data Czars
#######################################

Data czars should adopt and implement industry standard data security policies
and procedures and configure any computers and other devices that are used to
access, store, and work with learner data from edX.

EdX has prepared these guidelines for use as a starting point; they can and
should be used in conjunction with the member's own security program. EdX may
periodically update these guidelines to reflect changes in best practices.

.. contents::
  :local:
  :depth: 1

****************************
Who Should Be the Data Czar?
****************************

The data czar should be a person on staff who is able to fulfill the following
responsibilities.

* Prepared to serve as the single point of contact and accountability for
  receiving, handling, and distributing edX learner data.

* Responsible for managing the set of credentials used to decrypt learner data
  from edX.

* Knowledgeable about both technical and policy oriented security issues
  related to handling learner data.

For example, some member institutions name an academic professional or director
level researcher with security expertise, and others use their chief technical
officers.

For more information about the general and technical skills used by data czars,
see :ref:`Skills_Experience_Data_Czar`.

**********************************
How Should Credentials Be Managed?
**********************************

As a rule, data czars should not share the single set of credentials issued
by edX for decrypting learner data. However, edX recognizes that a data czar
may need to be supported or replaced by a colleague or other responsible staff
person on a limited and case-specific basis. Example situations in which such
support or replacement might be needed follow.

* An extended absence, such as a vacation or leave.

* A demanding workload for data management, such as frequent requests.

* A special project that involves burdensome data needs, such as daily
  downloads.

In such cases, the data czar should submit a request to edX that includes the
following information.

* The name of the person to add.

* The reason for the request.

* The expected length of time for which modified access is needed.

EdX handles such requests on a case-by-case basis.

.. note:: EdX may retire and refresh member credentials on a periodic basis
 and will notify affected data czars accordingly.

**********************************
How Should Learner Data Be Stored?
**********************************

EdX recommends the following procedures for storing learner data.

* Store and transfer learner data using an Open-PGP compatible encryption tool
  (for example, https://www.gnupg.org/download/) on all applicable devices.

* Store learner data only on devices that employ full disk encryption:
  FileVault on Mac®, BitLocker on Windows®, and Linux unified key setup (LUKS)
  or similar on Linux® operating systems.

* Transfer learner data only to devices, accounts, or services that are owned
  by the member institution. Do not transfer learner data to any device,
  account, or service where a service provider or other third party can access
  the data or acquire any rights to use it.

* Protect learner data that is stored on a network accessible device with a
  hardware firewall to ensure that only authorized hosts can create network
  connections.

* Apply operating system and application security updates to any network
  connected device within 48 hours of release.

* Individual (not shared) user accounts must be used to access the learner
  data, in accordance with organizational password or passphrase policies. If
  no policy exists, edX offers these guidelines.

  * Passwords should be at least 12 characters long and require three of the
    four following types of characters: uppercase, lowercase, numbers, special
    characters.

  * Passphrases should be at least 16 characters long, using any type of
    characters, but avoiding common phrases.

* Require all member researchers and other staff who access the learner data to
  use secure, locking screen savers that activate after a short period of
  inactivity (five minutes at most).

* Store learner data in a physically secure location (that is, in an office
  with a locked door, to which only staff with approval have access).

* Document a practice, known by the data czar and all of the member
  institution's researchers and other staff who access the learner data, to
  ensure that any possible security incident that might put the learner data at
  risk is reported to edX within twenty-four (24) hours.

* Document a practice, known and implemented by the data czar, to terminate
  access to learner data by staff who cease to be affiliated with the member
  institution.

* Conduct a periodic review of systems to ensure compliance with these
  guidelines.

Third parties that are engaged to support a permissible use of learner data
must be contractually bound to such use in accordance with security measures
that are consistent with those listed above.

**************************************************************************
What Are Some Best Practices for Use of Learner Data in Academic Research?
**************************************************************************

EdX supports the use of learner data to conduct scientific research, including
research in the areas of cognitive science and education. Example research
projects might evaluate the impact of edX on the worldwide educational
community to improve education on campus and online, or analyze statistics on
student performance and how students learn. EdX is also interested in hearing
about other potential areas of research.

Permissible uses of learner data are subject to your membership agreement with
edX, the edX `privacy policy`_, and the edX `best practices for communicating
with learners`_, (each as updated from time to time), and all applicable
privacy and data security laws.

* Use of learner data in academic research should be reviewed by your
  institutional review board (IRB) for approval or exemption, as appropriate.

* Data elements that contain identifiable or potentially identifiable
  information should be removed from datasets used in academic research, when
  feasible. While this will not de-identify the data against attackers, it can
  help prevent casual errors, such as including real names in a sociogram, or
  accidentally identifying a research colleague.

* Researchers should not re-identify or attempt to re-identify any
  de-identified learner data, including by combining them with other data sets,
  without written permission from the institution data czar, who should consult
  with edX for guidance as needed.

* Academic researchers should not contact any individuals whose information may
  be contained within the data without first obtaining appropriate written
  permission from the institution data czar who should consult with edX for
  guidance as needed.

* Academic research reports, abstracts, papers, and other findings should not
  include identifiable or potentially identifiable information. Academic
  research findings should also avoid presenting information that permits
  re-identification of any learner data.

* Academic research findings may contain an aggregation or summary of
  information contained within the data or other analysis of such information
  in graphical, tabular, or written form.

* Academic researchers should be careful to avoid using learner data in any way
  that is unlawful, defamatory, or libelous to learners, course team members,
  or others.

.. _privacy policy: https://www.edx.org/edx-privacy-policy
.. _best practices for communicating with learners: https://partners.edx.org/running-your-course/communicating-with-learners
