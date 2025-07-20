# test_data.py
from .db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

try:
    cursor.executescript("""
    INSERT INTO School Values('sc_joni1','Jokiniemen Koulu');
    INSERT INTO Teacher Values('t_mikavanhamki_joni','Mika Vanhamäki','+3584125499', 'mika.vanhamaki@eduvantaa.fi', '1234', 'sc_joni1' );
    INSERT INTO Class VALUES("cl_ma_7a_202507210815_202507210900_dur_45_rm_a101", "Mathematics", "7A", "2025-07-21 08:15", "2025-07-21 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507210815_202507210900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202507210900_202507210945_dur_45_rm_b204", "Chemistry", "8B", "2025-07-21 09:00", "2025-07-21 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202507210900_202507210945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202507211000_202507211045_dur_45_rm_a102", "Mathematics", "7B", "2025-07-21 10:00", "2025-07-21 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507211000_202507211045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202507211100_202507211145_dur_45_rm_b205", "Chemistry", "9A", "2025-07-21 11:00", "2025-07-21 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202507211100_202507211145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202507211230_202507211315_dur_45_rm_a103", "Math", "8C", "2025-07-21 12:30", "2025-07-21 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507211230_202507211315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202507280815_202507280900_dur_45_rm_a101", "Mathematics", "7A", "2025-07-28 08:15", "2025-07-28 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507280815_202507280900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202507280900_202507280945_dur_45_rm_b204", "Chemistry", "8B", "2025-07-28 09:00", "2025-07-28 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202507280900_202507280945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202507281000_202507281045_dur_45_rm_a102", "Mathematics", "7B", "2025-07-28 10:00", "2025-07-28 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507281000_202507281045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202507281100_202507281145_dur_45_rm_b205", "Chemistry", "9A", "2025-07-28 11:00", "2025-07-28 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202507281100_202507281145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202507281230_202507281315_dur_45_rm_a103", "Math", "8C", "2025-07-28 12:30", "2025-07-28 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507281230_202507281315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202508040815_202508040900_dur_45_rm_a101", "Mathematics", "7A", "2025-08-04 08:15", "2025-08-04 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508040815_202508040900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202508040900_202508040945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-04 09:00", "2025-08-04 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508040900_202508040945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202508041000_202508041045_dur_45_rm_a102", "Mathematics", "7B", "2025-08-04 10:00", "2025-08-04 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508041000_202508041045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202508041100_202508041145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-04 11:00", "2025-08-04 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508041100_202508041145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202508041230_202508041315_dur_45_rm_a103", "Math", "8C", "2025-08-04 12:30", "2025-08-04 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508041230_202508041315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202508110815_202508110900_dur_45_rm_a101", "Mathematics", "7A", "2025-08-11 08:15", "2025-08-11 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508110815_202508110900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202508110900_202508110945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-11 09:00", "2025-08-11 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508110900_202508110945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202508111000_202508111045_dur_45_rm_a102", "Mathematics", "7B", "2025-08-11 10:00", "2025-08-11 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508111000_202508111045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202508111100_202508111145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-11 11:00", "2025-08-11 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508111100_202508111145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202508111230_202508111315_dur_45_rm_a103", "Math", "8C", "2025-08-11 12:30", "2025-08-11 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508111230_202508111315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202508180815_202508180900_dur_45_rm_a101", "Mathematics", "7A", "2025-08-18 08:15", "2025-08-18 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508180815_202508180900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202508180900_202508180945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-18 09:00", "2025-08-18 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508180900_202508180945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202508181000_202508181045_dur_45_rm_a102", "Mathematics", "7B", "2025-08-18 10:00", "2025-08-18 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508181000_202508181045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202508181100_202508181145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-18 11:00", "2025-08-18 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508181100_202508181145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202508181230_202508181315_dur_45_rm_a103", "Math", "8C", "2025-08-18 12:30", "2025-08-18 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508181230_202508181315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202508250815_202508250900_dur_45_rm_a101", "Mathematics", "7A", "2025-08-25 08:15", "2025-08-25 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508250815_202508250900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202508250900_202508250945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-25 09:00", "2025-08-25 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508250900_202508250945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202508251000_202508251045_dur_45_rm_a102", "Mathematics", "7B", "2025-08-25 10:00", "2025-08-25 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508251000_202508251045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202508251100_202508251145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-25 11:00", "2025-08-25 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508251100_202508251145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202508251230_202508251315_dur_45_rm_a103", "Math", "8C", "2025-08-25 12:30", "2025-08-25 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508251230_202508251315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202509010815_202509010900_dur_45_rm_a101", "Mathematics", "7A", "2025-09-01 08:15", "2025-09-01 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509010815_202509010900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202509010900_202509010945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-01 09:00", "2025-09-01 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509010900_202509010945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202509011000_202509011045_dur_45_rm_a102", "Mathematics", "7B", "2025-09-01 10:00", "2025-09-01 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509011000_202509011045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202509011100_202509011145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-01 11:00", "2025-09-01 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509011100_202509011145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202509011230_202509011315_dur_45_rm_a103", "Math", "8C", "2025-09-01 12:30", "2025-09-01 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509011230_202509011315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202509080815_202509080900_dur_45_rm_a101", "Mathematics", "7A", "2025-09-08 08:15", "2025-09-08 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509080815_202509080900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202509080900_202509080945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-08 09:00", "2025-09-08 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509080900_202509080945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202509081000_202509081045_dur_45_rm_a102", "Mathematics", "7B", "2025-09-08 10:00", "2025-09-08 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509081000_202509081045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202509081100_202509081145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-08 11:00", "2025-09-08 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509081100_202509081145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202509081230_202509081315_dur_45_rm_a103", "Math", "8C", "2025-09-08 12:30", "2025-09-08 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509081230_202509081315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202509150815_202509150900_dur_45_rm_a101", "Mathematics", "7A", "2025-09-15 08:15", "2025-09-15 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509150815_202509150900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202509150900_202509150945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-15 09:00", "2025-09-15 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509150900_202509150945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202509151000_202509151045_dur_45_rm_a102", "Mathematics", "7B", "2025-09-15 10:00", "2025-09-15 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509151000_202509151045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202509151100_202509151145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-15 11:00", "2025-09-15 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509151100_202509151145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202509151230_202509151315_dur_45_rm_a103", "Math", "8C", "2025-09-15 12:30", "2025-09-15 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509151230_202509151315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202509220815_202509220900_dur_45_rm_a101", "Mathematics", "7A", "2025-09-22 08:15", "2025-09-22 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509220815_202509220900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202509220900_202509220945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-22 09:00", "2025-09-22 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509220900_202509220945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202509221000_202509221045_dur_45_rm_a102", "Mathematics", "7B", "2025-09-22 10:00", "2025-09-22 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509221000_202509221045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202509221100_202509221145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-22 11:00", "2025-09-22 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509221100_202509221145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202509221230_202509221315_dur_45_rm_a103", "Math", "8C", "2025-09-22 12:30", "2025-09-22 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509221230_202509221315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202509290815_202509290900_dur_45_rm_a101", "Mathematics", "7A", "2025-09-29 08:15", "2025-09-29 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509290815_202509290900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202509290900_202509290945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-29 09:00", "2025-09-29 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509290900_202509290945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202509291000_202509291045_dur_45_rm_a102", "Mathematics", "7B", "2025-09-29 10:00", "2025-09-29 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509291000_202509291045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202509291100_202509291145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-29 11:00", "2025-09-29 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509291100_202509291145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202509291230_202509291315_dur_45_rm_a103", "Math", "8C", "2025-09-29 12:30", "2025-09-29 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509291230_202509291315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202510060815_202510060900_dur_45_rm_a101", "Mathematics", "7A", "2025-10-06 08:15", "2025-10-06 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510060815_202510060900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202510060900_202510060945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-06 09:00", "2025-10-06 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510060900_202510060945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202510061000_202510061045_dur_45_rm_a102", "Mathematics", "7B", "2025-10-06 10:00", "2025-10-06 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510061000_202510061045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202510061100_202510061145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-06 11:00", "2025-10-06 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510061100_202510061145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202510061230_202510061315_dur_45_rm_a103", "Math", "8C", "2025-10-06 12:30", "2025-10-06 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510061230_202510061315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202510130815_202510130900_dur_45_rm_a101", "Mathematics", "7A", "2025-10-13 08:15", "2025-10-13 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510130815_202510130900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202510130900_202510130945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-13 09:00", "2025-10-13 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510130900_202510130945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202510131000_202510131045_dur_45_rm_a102", "Mathematics", "7B", "2025-10-13 10:00", "2025-10-13 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510131000_202510131045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202510131100_202510131145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-13 11:00", "2025-10-13 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510131100_202510131145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202510131230_202510131315_dur_45_rm_a103", "Math", "8C", "2025-10-13 12:30", "2025-10-13 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510131230_202510131315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202510200815_202510200900_dur_45_rm_a101", "Mathematics", "7A", "2025-10-20 08:15", "2025-10-20 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510200815_202510200900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202510200900_202510200945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-20 09:00", "2025-10-20 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510200900_202510200945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202510201000_202510201045_dur_45_rm_a102", "Mathematics", "7B", "2025-10-20 10:00", "2025-10-20 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510201000_202510201045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202510201100_202510201145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-20 11:00", "2025-10-20 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510201100_202510201145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202510201230_202510201315_dur_45_rm_a103", "Math", "8C", "2025-10-20 12:30", "2025-10-20 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510201230_202510201315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202510270815_202510270900_dur_45_rm_a101", "Mathematics", "7A", "2025-10-27 08:15", "2025-10-27 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510270815_202510270900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202510270900_202510270945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-27 09:00", "2025-10-27 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510270900_202510270945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202510271000_202510271045_dur_45_rm_a102", "Mathematics", "7B", "2025-10-27 10:00", "2025-10-27 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510271000_202510271045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202510271100_202510271145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-27 11:00", "2025-10-27 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510271100_202510271145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202510271230_202510271315_dur_45_rm_a103", "Math", "8C", "2025-10-27 12:30", "2025-10-27 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510271230_202510271315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511030815_202511030900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-03 08:15", "2025-11-03 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511030815_202511030900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511030900_202511030945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-03 09:00", "2025-11-03 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511030900_202511030945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511031000_202511031045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-03 10:00", "2025-11-03 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511031000_202511031045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511031100_202511031145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-03 11:00", "2025-11-03 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511031100_202511031145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511031230_202511031315_dur_45_rm_a103", "Math", "8C", "2025-11-03 12:30", "2025-11-03 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511031230_202511031315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511100815_202511100900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-10 08:15", "2025-11-10 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511100815_202511100900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511100900_202511100945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-10 09:00", "2025-11-10 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511100900_202511100945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511101000_202511101045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-10 10:00", "2025-11-10 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511101000_202511101045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511101100_202511101145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-10 11:00", "2025-11-10 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511101100_202511101145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511101230_202511101315_dur_45_rm_a103", "Math", "8C", "2025-11-10 12:30", "2025-11-10 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511101230_202511101315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511170815_202511170900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-17 08:15", "2025-11-17 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511170815_202511170900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511170900_202511170945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-17 09:00", "2025-11-17 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511170900_202511170945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511171000_202511171045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-17 10:00", "2025-11-17 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511171000_202511171045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511171100_202511171145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-17 11:00", "2025-11-17 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511171100_202511171145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511171230_202511171315_dur_45_rm_a103", "Math", "8C", "2025-11-17 12:30", "2025-11-17 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511171230_202511171315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511240815_202511240900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-24 08:15", "2025-11-24 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511240815_202511240900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511240900_202511240945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-24 09:00", "2025-11-24 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511240900_202511240945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511241000_202511241045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-24 10:00", "2025-11-24 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511241000_202511241045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511241100_202511241145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-24 11:00", "2025-11-24 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511241100_202511241145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511241230_202511241315_dur_45_rm_a103", "Math", "8C", "2025-11-24 12:30", "2025-11-24 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511241230_202511241315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512010815_202512010900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-01 08:15", "2025-12-01 09:00", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512010815_202512010900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512010900_202512010945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-01 09:00", "2025-12-01 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512010900_202512010945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512011000_202512011045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-01 10:00", "2025-12-01 10:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512011000_202512011045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512011100_202512011145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-01 11:00", "2025-12-01 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512011100_202512011145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512011230_202512011315_dur_45_rm_a103", "Math", "8C", "2025-12-01 12:30", "2025-12-01 13:15", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512011230_202512011315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ph_7c_202507220815_202507220900_dur_45_rm_a104", "Physics", "7C", "2025-07-22 08:15", "2025-07-22 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202507220815_202507220900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202507220900_202507220945_dur_45_rm_a105", "Physics", "8A", "2025-07-22 09:00", "2025-07-22 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202507220900_202507220945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202507221000_202507221045_dur_45_rm_gym1", "Physics", "9B", "2025-07-22 10:00", "2025-07-22 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202507221000_202507221045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202507221100_202507221145_dur_45_rm_a101", "Mathematics", "7A", "2025-07-22 11:00", "2025-07-22 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507221100_202507221145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202507290815_202507290900_dur_45_rm_a104", "Physics", "7C", "2025-07-29 08:15", "2025-07-29 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202507290815_202507290900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202507290900_202507290945_dur_45_rm_a105", "Physics", "8A", "2025-07-29 09:00", "2025-07-29 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202507290900_202507290945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202507291000_202507291045_dur_45_rm_gym1", "Physics", "9B", "2025-07-29 10:00", "2025-07-29 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202507291000_202507291045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202507291100_202507291145_dur_45_rm_a101", "Mathematics", "7A", "2025-07-29 11:00", "2025-07-29 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507291100_202507291145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202508050815_202508050900_dur_45_rm_a104", "Physics", "7C", "2025-08-05 08:15", "2025-08-05 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508050815_202508050900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202508050900_202508050945_dur_45_rm_a105", "Physics", "8A", "2025-08-05 09:00", "2025-08-05 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508050900_202508050945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202508051000_202508051045_dur_45_rm_gym1", "Physics", "9B", "2025-08-05 10:00", "2025-08-05 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508051000_202508051045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202508051100_202508051145_dur_45_rm_a101", "Mathematics", "7A", "2025-08-05 11:00", "2025-08-05 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508051100_202508051145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202508120815_202508120900_dur_45_rm_a104", "Physics", "7C", "2025-08-12 08:15", "2025-08-12 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508120815_202508120900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202508120900_202508120945_dur_45_rm_a105", "Physics", "8A", "2025-08-12 09:00", "2025-08-12 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508120900_202508120945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202508121000_202508121045_dur_45_rm_gym1", "Physics", "9B", "2025-08-12 10:00", "2025-08-12 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508121000_202508121045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202508121100_202508121145_dur_45_rm_a101", "Mathematics", "7A", "2025-08-12 11:00", "2025-08-12 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508121100_202508121145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202508190815_202508190900_dur_45_rm_a104", "Physics", "7C", "2025-08-19 08:15", "2025-08-19 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508190815_202508190900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202508190900_202508190945_dur_45_rm_a105", "Physics", "8A", "2025-08-19 09:00", "2025-08-19 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508190900_202508190945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202508191000_202508191045_dur_45_rm_gym1", "Physics", "9B", "2025-08-19 10:00", "2025-08-19 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508191000_202508191045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202508191100_202508191145_dur_45_rm_a101", "Mathematics", "7A", "2025-08-19 11:00", "2025-08-19 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508191100_202508191145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202508260815_202508260900_dur_45_rm_a104", "Physics", "7C", "2025-08-26 08:15", "2025-08-26 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508260815_202508260900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202508260900_202508260945_dur_45_rm_a105", "Physics", "8A", "2025-08-26 09:00", "2025-08-26 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508260900_202508260945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202508261000_202508261045_dur_45_rm_gym1", "Physics", "9B", "2025-08-26 10:00", "2025-08-26 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508261000_202508261045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202508261100_202508261145_dur_45_rm_a101", "Mathematics", "7A", "2025-08-26 11:00", "2025-08-26 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508261100_202508261145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202509020815_202509020900_dur_45_rm_a104", "Physics", "7C", "2025-09-02 08:15", "2025-09-02 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509020815_202509020900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202509020900_202509020945_dur_45_rm_a105", "Physics", "8A", "2025-09-02 09:00", "2025-09-02 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509020900_202509020945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202509021000_202509021045_dur_45_rm_gym1", "Physics", "9B", "2025-09-02 10:00", "2025-09-02 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509021000_202509021045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202509021100_202509021145_dur_45_rm_a101", "Mathematics", "7A", "2025-09-02 11:00", "2025-09-02 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509021100_202509021145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202509090815_202509090900_dur_45_rm_a104", "Physics", "7C", "2025-09-09 08:15", "2025-09-09 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509090815_202509090900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202509090900_202509090945_dur_45_rm_a105", "Physics", "8A", "2025-09-09 09:00", "2025-09-09 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509090900_202509090945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202509091000_202509091045_dur_45_rm_gym1", "Physics", "9B", "2025-09-09 10:00", "2025-09-09 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509091000_202509091045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202509091100_202509091145_dur_45_rm_a101", "Mathematics", "7A", "2025-09-09 11:00", "2025-09-09 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509091100_202509091145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202509160815_202509160900_dur_45_rm_a104", "Physics", "7C", "2025-09-16 08:15", "2025-09-16 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509160815_202509160900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202509160900_202509160945_dur_45_rm_a105", "Physics", "8A", "2025-09-16 09:00", "2025-09-16 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509160900_202509160945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202509161000_202509161045_dur_45_rm_gym1", "Physics", "9B", "2025-09-16 10:00", "2025-09-16 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509161000_202509161045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202509161100_202509161145_dur_45_rm_a101", "Mathematics", "7A", "2025-09-16 11:00", "2025-09-16 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509161100_202509161145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202509230815_202509230900_dur_45_rm_a104", "Physics", "7C", "2025-09-23 08:15", "2025-09-23 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509230815_202509230900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202509230900_202509230945_dur_45_rm_a105", "Physics", "8A", "2025-09-23 09:00", "2025-09-23 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509230900_202509230945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202509231000_202509231045_dur_45_rm_gym1", "Physics", "9B", "2025-09-23 10:00", "2025-09-23 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509231000_202509231045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202509231100_202509231145_dur_45_rm_a101", "Mathematics", "7A", "2025-09-23 11:00", "2025-09-23 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509231100_202509231145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202509300815_202509300900_dur_45_rm_a104", "Physics", "7C", "2025-09-30 08:15", "2025-09-30 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509300815_202509300900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202509300900_202509300945_dur_45_rm_a105", "Physics", "8A", "2025-09-30 09:00", "2025-09-30 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509300900_202509300945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202509301000_202509301045_dur_45_rm_gym1", "Physics", "9B", "2025-09-30 10:00", "2025-09-30 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509301000_202509301045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202509301100_202509301145_dur_45_rm_a101", "Mathematics", "7A", "2025-09-30 11:00", "2025-09-30 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509301100_202509301145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202510070815_202510070900_dur_45_rm_a104", "Physics", "7C", "2025-10-07 08:15", "2025-10-07 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510070815_202510070900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202510070900_202510070945_dur_45_rm_a105", "Physics", "8A", "2025-10-07 09:00", "2025-10-07 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510070900_202510070945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202510071000_202510071045_dur_45_rm_gym1", "Physics", "9B", "2025-10-07 10:00", "2025-10-07 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510071000_202510071045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202510071100_202510071145_dur_45_rm_a101", "Mathematics", "7A", "2025-10-07 11:00", "2025-10-07 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510071100_202510071145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202510140815_202510140900_dur_45_rm_a104", "Physics", "7C", "2025-10-14 08:15", "2025-10-14 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510140815_202510140900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202510140900_202510140945_dur_45_rm_a105", "Physics", "8A", "2025-10-14 09:00", "2025-10-14 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510140900_202510140945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202510141000_202510141045_dur_45_rm_gym1", "Physics", "9B", "2025-10-14 10:00", "2025-10-14 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510141000_202510141045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202510141100_202510141145_dur_45_rm_a101", "Mathematics", "7A", "2025-10-14 11:00", "2025-10-14 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510141100_202510141145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202510210815_202510210900_dur_45_rm_a104", "Physics", "7C", "2025-10-21 08:15", "2025-10-21 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510210815_202510210900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202510210900_202510210945_dur_45_rm_a105", "Physics", "8A", "2025-10-21 09:00", "2025-10-21 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510210900_202510210945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202510211000_202510211045_dur_45_rm_gym1", "Physics", "9B", "2025-10-21 10:00", "2025-10-21 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510211000_202510211045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202510211100_202510211145_dur_45_rm_a101", "Mathematics", "7A", "2025-10-21 11:00", "2025-10-21 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510211100_202510211145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202510280815_202510280900_dur_45_rm_a104", "Physics", "7C", "2025-10-28 08:15", "2025-10-28 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510280815_202510280900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202510280900_202510280945_dur_45_rm_a105", "Physics", "8A", "2025-10-28 09:00", "2025-10-28 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510280900_202510280945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202510281000_202510281045_dur_45_rm_gym1", "Physics", "9B", "2025-10-28 10:00", "2025-10-28 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510281000_202510281045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202510281100_202510281145_dur_45_rm_a101", "Mathematics", "7A", "2025-10-28 11:00", "2025-10-28 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510281100_202510281145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511040815_202511040900_dur_45_rm_a104", "Physics", "7C", "2025-11-04 08:15", "2025-11-04 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511040815_202511040900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511040900_202511040945_dur_45_rm_a105", "Physics", "8A", "2025-11-04 09:00", "2025-11-04 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511040900_202511040945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511041000_202511041045_dur_45_rm_gym1", "Physics", "9B", "2025-11-04 10:00", "2025-11-04 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511041000_202511041045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511041100_202511041145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-04 11:00", "2025-11-04 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511041100_202511041145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511110815_202511110900_dur_45_rm_a104", "Physics", "7C", "2025-11-11 08:15", "2025-11-11 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511110815_202511110900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511110900_202511110945_dur_45_rm_a105", "Physics", "8A", "2025-11-11 09:00", "2025-11-11 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511110900_202511110945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511111000_202511111045_dur_45_rm_gym1", "Physics", "9B", "2025-11-11 10:00", "2025-11-11 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511111000_202511111045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511111100_202511111145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-11 11:00", "2025-11-11 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511111100_202511111145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511180815_202511180900_dur_45_rm_a104", "Physics", "7C", "2025-11-18 08:15", "2025-11-18 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511180815_202511180900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511180900_202511180945_dur_45_rm_a105", "Physics", "8A", "2025-11-18 09:00", "2025-11-18 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511180900_202511180945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511181000_202511181045_dur_45_rm_gym1", "Physics", "9B", "2025-11-18 10:00", "2025-11-18 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511181000_202511181045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511181100_202511181145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-18 11:00", "2025-11-18 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511181100_202511181145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511250815_202511250900_dur_45_rm_a104", "Physics", "7C", "2025-11-25 08:15", "2025-11-25 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511250815_202511250900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511250900_202511250945_dur_45_rm_a105", "Physics", "8A", "2025-11-25 09:00", "2025-11-25 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511250900_202511250945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511251000_202511251045_dur_45_rm_gym1", "Physics", "9B", "2025-11-25 10:00", "2025-11-25 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511251000_202511251045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511251100_202511251145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-25 11:00", "2025-11-25 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511251100_202511251145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512020815_202512020900_dur_45_rm_a104", "Physics", "7C", "2025-12-02 08:15", "2025-12-02 09:00", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512020815_202512020900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512020900_202512020945_dur_45_rm_a105", "Physics", "8A", "2025-12-02 09:00", "2025-12-02 09:45", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512020900_202512020945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512021000_202512021045_dur_45_rm_gym1", "Physics", "9B", "2025-12-02 10:00", "2025-12-02 10:45", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512021000_202512021045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512021100_202512021145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-02 11:00", "2025-12-02 11:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512021100_202512021145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ma_8c_202507230815_202507230900_dur_45_rm_a103", "Mathematics", "8C", "2025-07-23 08:15", "2025-07-23 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507230815_202507230900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202507230900_202507230945_dur_45_rm_a102", "Mathematics", "7B", "2025-07-23 09:00", "2025-07-23 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507230900_202507230945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202507231000_202507231045_dur_45_rm_b204", "Chemistry", "8B", "2025-07-23 10:00", "2025-07-23 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202507231000_202507231045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202507231100_202507231145_dur_45_rm_b205", "Chemistry", "9A", "2025-07-23 11:00", "2025-07-23 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202507231100_202507231145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202507231230_202507231315_dur_45_rm_a105", "Physics", "8A", "2025-07-23 12:30", "2025-07-23 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202507231230_202507231315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202507300815_202507300900_dur_45_rm_a103", "Mathematics", "8C", "2025-07-30 08:15", "2025-07-30 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507300815_202507300900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202507300900_202507300945_dur_45_rm_a102", "Mathematics", "7B", "2025-07-30 09:00", "2025-07-30 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507300900_202507300945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202507301000_202507301045_dur_45_rm_b204", "Chemistry", "8B", "2025-07-30 10:00", "2025-07-30 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202507301000_202507301045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202507301100_202507301145_dur_45_rm_b205", "Chemistry", "9A", "2025-07-30 11:00", "2025-07-30 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202507301100_202507301145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202507301230_202507301315_dur_45_rm_a105", "Physics", "8A", "2025-07-30 12:30", "2025-07-30 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202507301230_202507301315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202508060815_202508060900_dur_45_rm_a103", "Mathematics", "8C", "2025-08-06 08:15", "2025-08-06 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508060815_202508060900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508060900_202508060945_dur_45_rm_a102", "Mathematics", "7B", "2025-08-06 09:00", "2025-08-06 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508060900_202508060945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202508061000_202508061045_dur_45_rm_b204", "Chemistry", "8B", "2025-08-06 10:00", "2025-08-06 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508061000_202508061045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508061100_202508061145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-06 11:00", "2025-08-06 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508061100_202508061145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202508061230_202508061315_dur_45_rm_a105", "Physics", "8A", "2025-08-06 12:30", "2025-08-06 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508061230_202508061315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202508130815_202508130900_dur_45_rm_a103", "Mathematics", "8C", "2025-08-13 08:15", "2025-08-13 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508130815_202508130900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508130900_202508130945_dur_45_rm_a102", "Mathematics", "7B", "2025-08-13 09:00", "2025-08-13 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508130900_202508130945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202508131000_202508131045_dur_45_rm_b204", "Chemistry", "8B", "2025-08-13 10:00", "2025-08-13 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508131000_202508131045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508131100_202508131145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-13 11:00", "2025-08-13 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508131100_202508131145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202508131230_202508131315_dur_45_rm_a105", "Physics", "8A", "2025-08-13 12:30", "2025-08-13 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508131230_202508131315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202508200815_202508200900_dur_45_rm_a103", "Mathematics", "8C", "2025-08-20 08:15", "2025-08-20 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508200815_202508200900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508200900_202508200945_dur_45_rm_a102", "Mathematics", "7B", "2025-08-20 09:00", "2025-08-20 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508200900_202508200945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202508201000_202508201045_dur_45_rm_b204", "Chemistry", "8B", "2025-08-20 10:00", "2025-08-20 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508201000_202508201045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508201100_202508201145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-20 11:00", "2025-08-20 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508201100_202508201145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202508201230_202508201315_dur_45_rm_a105", "Physics", "8A", "2025-08-20 12:30", "2025-08-20 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508201230_202508201315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202508270815_202508270900_dur_45_rm_a103", "Mathematics", "8C", "2025-08-27 08:15", "2025-08-27 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508270815_202508270900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508270900_202508270945_dur_45_rm_a102", "Mathematics", "7B", "2025-08-27 09:00", "2025-08-27 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508270900_202508270945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202508271000_202508271045_dur_45_rm_b204", "Chemistry", "8B", "2025-08-27 10:00", "2025-08-27 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508271000_202508271045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508271100_202508271145_dur_45_rm_b205", "Chemistry", "9A", "2025-08-27 11:00", "2025-08-27 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508271100_202508271145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202508271230_202508271315_dur_45_rm_a105", "Physics", "8A", "2025-08-27 12:30", "2025-08-27 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508271230_202508271315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202509030815_202509030900_dur_45_rm_a103", "Mathematics", "8C", "2025-09-03 08:15", "2025-09-03 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509030815_202509030900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509030900_202509030945_dur_45_rm_a102", "Mathematics", "7B", "2025-09-03 09:00", "2025-09-03 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509030900_202509030945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202509031000_202509031045_dur_45_rm_b204", "Chemistry", "8B", "2025-09-03 10:00", "2025-09-03 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509031000_202509031045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509031100_202509031145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-03 11:00", "2025-09-03 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509031100_202509031145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202509031230_202509031315_dur_45_rm_a105", "Physics", "8A", "2025-09-03 12:30", "2025-09-03 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509031230_202509031315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202509100815_202509100900_dur_45_rm_a103", "Mathematics", "8C", "2025-09-10 08:15", "2025-09-10 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509100815_202509100900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509100900_202509100945_dur_45_rm_a102", "Mathematics", "7B", "2025-09-10 09:00", "2025-09-10 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509100900_202509100945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202509101000_202509101045_dur_45_rm_b204", "Chemistry", "8B", "2025-09-10 10:00", "2025-09-10 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509101000_202509101045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509101100_202509101145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-10 11:00", "2025-09-10 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509101100_202509101145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202509101230_202509101315_dur_45_rm_a105", "Physics", "8A", "2025-09-10 12:30", "2025-09-10 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509101230_202509101315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202509170815_202509170900_dur_45_rm_a103", "Mathematics", "8C", "2025-09-17 08:15", "2025-09-17 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509170815_202509170900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509170900_202509170945_dur_45_rm_a102", "Mathematics", "7B", "2025-09-17 09:00", "2025-09-17 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509170900_202509170945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202509171000_202509171045_dur_45_rm_b204", "Chemistry", "8B", "2025-09-17 10:00", "2025-09-17 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509171000_202509171045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509171100_202509171145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-17 11:00", "2025-09-17 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509171100_202509171145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202509171230_202509171315_dur_45_rm_a105", "Physics", "8A", "2025-09-17 12:30", "2025-09-17 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509171230_202509171315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202509240815_202509240900_dur_45_rm_a103", "Mathematics", "8C", "2025-09-24 08:15", "2025-09-24 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509240815_202509240900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509240900_202509240945_dur_45_rm_a102", "Mathematics", "7B", "2025-09-24 09:00", "2025-09-24 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509240900_202509240945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202509241000_202509241045_dur_45_rm_b204", "Chemistry", "8B", "2025-09-24 10:00", "2025-09-24 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509241000_202509241045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509241100_202509241145_dur_45_rm_b205", "Chemistry", "9A", "2025-09-24 11:00", "2025-09-24 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509241100_202509241145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202509241230_202509241315_dur_45_rm_a105", "Physics", "8A", "2025-09-24 12:30", "2025-09-24 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509241230_202509241315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202510010815_202510010900_dur_45_rm_a103", "Mathematics", "8C", "2025-10-01 08:15", "2025-10-01 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510010815_202510010900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510010900_202510010945_dur_45_rm_a102", "Mathematics", "7B", "2025-10-01 09:00", "2025-10-01 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510010900_202510010945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202510011000_202510011045_dur_45_rm_b204", "Chemistry", "8B", "2025-10-01 10:00", "2025-10-01 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510011000_202510011045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510011100_202510011145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-01 11:00", "2025-10-01 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510011100_202510011145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202510011230_202510011315_dur_45_rm_a105", "Physics", "8A", "2025-10-01 12:30", "2025-10-01 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510011230_202510011315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202510080815_202510080900_dur_45_rm_a103", "Mathematics", "8C", "2025-10-08 08:15", "2025-10-08 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510080815_202510080900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510080900_202510080945_dur_45_rm_a102", "Mathematics", "7B", "2025-10-08 09:00", "2025-10-08 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510080900_202510080945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202510081000_202510081045_dur_45_rm_b204", "Chemistry", "8B", "2025-10-08 10:00", "2025-10-08 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510081000_202510081045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510081100_202510081145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-08 11:00", "2025-10-08 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510081100_202510081145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202510081230_202510081315_dur_45_rm_a105", "Physics", "8A", "2025-10-08 12:30", "2025-10-08 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510081230_202510081315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202510150815_202510150900_dur_45_rm_a103", "Mathematics", "8C", "2025-10-15 08:15", "2025-10-15 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510150815_202510150900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510150900_202510150945_dur_45_rm_a102", "Mathematics", "7B", "2025-10-15 09:00", "2025-10-15 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510150900_202510150945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202510151000_202510151045_dur_45_rm_b204", "Chemistry", "8B", "2025-10-15 10:00", "2025-10-15 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510151000_202510151045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510151100_202510151145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-15 11:00", "2025-10-15 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510151100_202510151145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202510151230_202510151315_dur_45_rm_a105", "Physics", "8A", "2025-10-15 12:30", "2025-10-15 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510151230_202510151315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202510220815_202510220900_dur_45_rm_a103", "Mathematics", "8C", "2025-10-22 08:15", "2025-10-22 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510220815_202510220900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510220900_202510220945_dur_45_rm_a102", "Mathematics", "7B", "2025-10-22 09:00", "2025-10-22 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510220900_202510220945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202510221000_202510221045_dur_45_rm_b204", "Chemistry", "8B", "2025-10-22 10:00", "2025-10-22 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510221000_202510221045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510221100_202510221145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-22 11:00", "2025-10-22 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510221100_202510221145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202510221230_202510221315_dur_45_rm_a105", "Physics", "8A", "2025-10-22 12:30", "2025-10-22 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510221230_202510221315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202510290815_202510290900_dur_45_rm_a103", "Mathematics", "8C", "2025-10-29 08:15", "2025-10-29 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510290815_202510290900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510290900_202510290945_dur_45_rm_a102", "Mathematics", "7B", "2025-10-29 09:00", "2025-10-29 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510290900_202510290945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202510291000_202510291045_dur_45_rm_b204", "Chemistry", "8B", "2025-10-29 10:00", "2025-10-29 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510291000_202510291045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510291100_202510291145_dur_45_rm_b205", "Chemistry", "9A", "2025-10-29 11:00", "2025-10-29 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510291100_202510291145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202510291230_202510291315_dur_45_rm_a105", "Physics", "8A", "2025-10-29 12:30", "2025-10-29 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510291230_202510291315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511050815_202511050900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-05 08:15", "2025-11-05 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511050815_202511050900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511050900_202511050945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-05 09:00", "2025-11-05 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511050900_202511050945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511051000_202511051045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-05 10:00", "2025-11-05 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511051000_202511051045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511051100_202511051145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-05 11:00", "2025-11-05 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511051100_202511051145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511051230_202511051315_dur_45_rm_a105", "Physics", "8A", "2025-11-05 12:30", "2025-11-05 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511051230_202511051315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511120815_202511120900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-12 08:15", "2025-11-12 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511120815_202511120900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511120900_202511120945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-12 09:00", "2025-11-12 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511120900_202511120945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511121000_202511121045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-12 10:00", "2025-11-12 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511121000_202511121045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511121100_202511121145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-12 11:00", "2025-11-12 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511121100_202511121145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511121230_202511121315_dur_45_rm_a105", "Physics", "8A", "2025-11-12 12:30", "2025-11-12 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511121230_202511121315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511190815_202511190900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-19 08:15", "2025-11-19 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511190815_202511190900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511190900_202511190945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-19 09:00", "2025-11-19 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511190900_202511190945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511191000_202511191045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-19 10:00", "2025-11-19 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511191000_202511191045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511191100_202511191145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-19 11:00", "2025-11-19 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511191100_202511191145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511191230_202511191315_dur_45_rm_a105", "Physics", "8A", "2025-11-19 12:30", "2025-11-19 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511191230_202511191315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511260815_202511260900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-26 08:15", "2025-11-26 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511260815_202511260900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511260900_202511260945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-26 09:00", "2025-11-26 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511260900_202511260945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511261000_202511261045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-26 10:00", "2025-11-26 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511261000_202511261045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511261100_202511261145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-26 11:00", "2025-11-26 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511261100_202511261145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511261230_202511261315_dur_45_rm_a105", "Physics", "8A", "2025-11-26 12:30", "2025-11-26 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511261230_202511261315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512030815_202512030900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-03 08:15", "2025-12-03 09:00", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512030815_202512030900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512030900_202512030945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-03 09:00", "2025-12-03 09:45", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512030900_202512030945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512031000_202512031045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-03 10:00", "2025-12-03 10:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512031000_202512031045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512031100_202512031145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-03 11:00", "2025-12-03 11:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512031100_202512031145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512031230_202512031315_dur_45_rm_a105", "Physics", "8A", "2025-12-03 12:30", "2025-12-03 13:15", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512031230_202512031315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ph_9b_202507240815_202507240900_dur_45_rm_gym1", "Physics", "9B", "2025-07-24 08:15", "2025-07-24 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202507240815_202507240900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202507240900_202507240945_dur_45_rm_a104", "Physics", "7C", "2025-07-24 09:00", "2025-07-24 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202507240900_202507240945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202507241000_202507241045_dur_45_rm_a101", "Mathematics", "7A", "2025-07-24 10:00", "2025-07-24 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507241000_202507241045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202507241100_202507241145_dur_45_rm_a103", "Mathematics", "8C", "2025-07-24 11:00", "2025-07-24 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507241100_202507241145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202507241230_202507241315_dur_45_rm_a102", "Mathematics", "7B", "2025-07-24 12:30", "2025-07-24 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507241230_202507241315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202507310815_202507310900_dur_45_rm_gym1", "Physics", "9B", "2025-07-31 08:15", "2025-07-31 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202507310815_202507310900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202507310900_202507310945_dur_45_rm_a104", "Physics", "7C", "2025-07-31 09:00", "2025-07-31 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202507310900_202507310945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202507311000_202507311045_dur_45_rm_a101", "Mathematics", "7A", "2025-07-31 10:00", "2025-07-31 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202507311000_202507311045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202507311100_202507311145_dur_45_rm_a103", "Mathematics", "8C", "2025-07-31 11:00", "2025-07-31 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202507311100_202507311145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202507311230_202507311315_dur_45_rm_a102", "Mathematics", "7B", "2025-07-31 12:30", "2025-07-31 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202507311230_202507311315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202508070815_202508070900_dur_45_rm_gym1", "Physics", "9B", "2025-08-07 08:15", "2025-08-07 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508070815_202508070900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202508070900_202508070945_dur_45_rm_a104", "Physics", "7C", "2025-08-07 09:00", "2025-08-07 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508070900_202508070945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202508071000_202508071045_dur_45_rm_a101", "Mathematics", "7A", "2025-08-07 10:00", "2025-08-07 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508071000_202508071045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202508071100_202508071145_dur_45_rm_a103", "Mathematics", "8C", "2025-08-07 11:00", "2025-08-07 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508071100_202508071145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508071230_202508071315_dur_45_rm_a102", "Mathematics", "7B", "2025-08-07 12:30", "2025-08-07 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508071230_202508071315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202508140815_202508140900_dur_45_rm_gym1", "Physics", "9B", "2025-08-14 08:15", "2025-08-14 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508140815_202508140900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202508140900_202508140945_dur_45_rm_a104", "Physics", "7C", "2025-08-14 09:00", "2025-08-14 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508140900_202508140945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202508141000_202508141045_dur_45_rm_a101", "Mathematics", "7A", "2025-08-14 10:00", "2025-08-14 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508141000_202508141045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202508141100_202508141145_dur_45_rm_a103", "Mathematics", "8C", "2025-08-14 11:00", "2025-08-14 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508141100_202508141145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508141230_202508141315_dur_45_rm_a102", "Mathematics", "7B", "2025-08-14 12:30", "2025-08-14 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508141230_202508141315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202508210815_202508210900_dur_45_rm_gym1", "Physics", "9B", "2025-08-21 08:15", "2025-08-21 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508210815_202508210900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202508210900_202508210945_dur_45_rm_a104", "Physics", "7C", "2025-08-21 09:00", "2025-08-21 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508210900_202508210945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202508211000_202508211045_dur_45_rm_a101", "Mathematics", "7A", "2025-08-21 10:00", "2025-08-21 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508211000_202508211045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202508211100_202508211145_dur_45_rm_a103", "Mathematics", "8C", "2025-08-21 11:00", "2025-08-21 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508211100_202508211145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508211230_202508211315_dur_45_rm_a102", "Mathematics", "7B", "2025-08-21 12:30", "2025-08-21 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508211230_202508211315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202508280815_202508280900_dur_45_rm_gym1", "Physics", "9B", "2025-08-28 08:15", "2025-08-28 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202508280815_202508280900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202508280900_202508280945_dur_45_rm_a104", "Physics", "7C", "2025-08-28 09:00", "2025-08-28 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508280900_202508280945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202508281000_202508281045_dur_45_rm_a101", "Mathematics", "7A", "2025-08-28 10:00", "2025-08-28 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202508281000_202508281045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202508281100_202508281145_dur_45_rm_a103", "Mathematics", "8C", "2025-08-28 11:00", "2025-08-28 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202508281100_202508281145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202508281230_202508281315_dur_45_rm_a102", "Mathematics", "7B", "2025-08-28 12:30", "2025-08-28 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202508281230_202508281315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202509040815_202509040900_dur_45_rm_gym1", "Physics", "9B", "2025-09-04 08:15", "2025-09-04 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509040815_202509040900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202509040900_202509040945_dur_45_rm_a104", "Physics", "7C", "2025-09-04 09:00", "2025-09-04 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509040900_202509040945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202509041000_202509041045_dur_45_rm_a101", "Mathematics", "7A", "2025-09-04 10:00", "2025-09-04 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509041000_202509041045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202509041100_202509041145_dur_45_rm_a103", "Mathematics", "8C", "2025-09-04 11:00", "2025-09-04 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509041100_202509041145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509041230_202509041315_dur_45_rm_a102", "Mathematics", "7B", "2025-09-04 12:30", "2025-09-04 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509041230_202509041315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202509110815_202509110900_dur_45_rm_gym1", "Physics", "9B", "2025-09-11 08:15", "2025-09-11 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509110815_202509110900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202509110900_202509110945_dur_45_rm_a104", "Physics", "7C", "2025-09-11 09:00", "2025-09-11 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509110900_202509110945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202509111000_202509111045_dur_45_rm_a101", "Mathematics", "7A", "2025-09-11 10:00", "2025-09-11 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509111000_202509111045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202509111100_202509111145_dur_45_rm_a103", "Mathematics", "8C", "2025-09-11 11:00", "2025-09-11 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509111100_202509111145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509111230_202509111315_dur_45_rm_a102", "Mathematics", "7B", "2025-09-11 12:30", "2025-09-11 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509111230_202509111315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202509180815_202509180900_dur_45_rm_gym1", "Physics", "9B", "2025-09-18 08:15", "2025-09-18 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509180815_202509180900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202509180900_202509180945_dur_45_rm_a104", "Physics", "7C", "2025-09-18 09:00", "2025-09-18 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509180900_202509180945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202509181000_202509181045_dur_45_rm_a101", "Mathematics", "7A", "2025-09-18 10:00", "2025-09-18 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509181000_202509181045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202509181100_202509181145_dur_45_rm_a103", "Mathematics", "8C", "2025-09-18 11:00", "2025-09-18 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509181100_202509181145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509181230_202509181315_dur_45_rm_a102", "Mathematics", "7B", "2025-09-18 12:30", "2025-09-18 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509181230_202509181315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202509250815_202509250900_dur_45_rm_gym1", "Physics", "9B", "2025-09-25 08:15", "2025-09-25 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202509250815_202509250900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202509250900_202509250945_dur_45_rm_a104", "Physics", "7C", "2025-09-25 09:00", "2025-09-25 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509250900_202509250945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202509251000_202509251045_dur_45_rm_a101", "Mathematics", "7A", "2025-09-25 10:00", "2025-09-25 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202509251000_202509251045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202509251100_202509251145_dur_45_rm_a103", "Mathematics", "8C", "2025-09-25 11:00", "2025-09-25 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202509251100_202509251145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202509251230_202509251315_dur_45_rm_a102", "Mathematics", "7B", "2025-09-25 12:30", "2025-09-25 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202509251230_202509251315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202510020815_202510020900_dur_45_rm_gym1", "Physics", "9B", "2025-10-02 08:15", "2025-10-02 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510020815_202510020900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202510020900_202510020945_dur_45_rm_a104", "Physics", "7C", "2025-10-02 09:00", "2025-10-02 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510020900_202510020945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202510021000_202510021045_dur_45_rm_a101", "Mathematics", "7A", "2025-10-02 10:00", "2025-10-02 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510021000_202510021045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202510021100_202510021145_dur_45_rm_a103", "Mathematics", "8C", "2025-10-02 11:00", "2025-10-02 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510021100_202510021145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510021230_202510021315_dur_45_rm_a102", "Mathematics", "7B", "2025-10-02 12:30", "2025-10-02 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510021230_202510021315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202510090815_202510090900_dur_45_rm_gym1", "Physics", "9B", "2025-10-09 08:15", "2025-10-09 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510090815_202510090900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202510090900_202510090945_dur_45_rm_a104", "Physics", "7C", "2025-10-09 09:00", "2025-10-09 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510090900_202510090945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202510091000_202510091045_dur_45_rm_a101", "Mathematics", "7A", "2025-10-09 10:00", "2025-10-09 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510091000_202510091045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202510091100_202510091145_dur_45_rm_a103", "Mathematics", "8C", "2025-10-09 11:00", "2025-10-09 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510091100_202510091145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510091230_202510091315_dur_45_rm_a102", "Mathematics", "7B", "2025-10-09 12:30", "2025-10-09 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510091230_202510091315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202510160815_202510160900_dur_45_rm_gym1", "Physics", "9B", "2025-10-16 08:15", "2025-10-16 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510160815_202510160900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202510160900_202510160945_dur_45_rm_a104", "Physics", "7C", "2025-10-16 09:00", "2025-10-16 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510160900_202510160945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202510161000_202510161045_dur_45_rm_a101", "Mathematics", "7A", "2025-10-16 10:00", "2025-10-16 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510161000_202510161045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202510161100_202510161145_dur_45_rm_a103", "Mathematics", "8C", "2025-10-16 11:00", "2025-10-16 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510161100_202510161145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510161230_202510161315_dur_45_rm_a102", "Mathematics", "7B", "2025-10-16 12:30", "2025-10-16 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510161230_202510161315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202510230815_202510230900_dur_45_rm_gym1", "Physics", "9B", "2025-10-23 08:15", "2025-10-23 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510230815_202510230900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202510230900_202510230945_dur_45_rm_a104", "Physics", "7C", "2025-10-23 09:00", "2025-10-23 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510230900_202510230945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202510231000_202510231045_dur_45_rm_a101", "Mathematics", "7A", "2025-10-23 10:00", "2025-10-23 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510231000_202510231045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202510231100_202510231145_dur_45_rm_a103", "Mathematics", "8C", "2025-10-23 11:00", "2025-10-23 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510231100_202510231145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510231230_202510231315_dur_45_rm_a102", "Mathematics", "7B", "2025-10-23 12:30", "2025-10-23 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510231230_202510231315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202510300815_202510300900_dur_45_rm_gym1", "Physics", "9B", "2025-10-30 08:15", "2025-10-30 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202510300815_202510300900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202510300900_202510300945_dur_45_rm_a104", "Physics", "7C", "2025-10-30 09:00", "2025-10-30 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510300900_202510300945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202510301000_202510301045_dur_45_rm_a101", "Mathematics", "7A", "2025-10-30 10:00", "2025-10-30 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202510301000_202510301045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202510301100_202510301145_dur_45_rm_a103", "Mathematics", "8C", "2025-10-30 11:00", "2025-10-30 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202510301100_202510301145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202510301230_202510301315_dur_45_rm_a102", "Mathematics", "7B", "2025-10-30 12:30", "2025-10-30 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202510301230_202510301315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511060815_202511060900_dur_45_rm_gym1", "Physics", "9B", "2025-11-06 08:15", "2025-11-06 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511060815_202511060900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511060900_202511060945_dur_45_rm_a104", "Physics", "7C", "2025-11-06 09:00", "2025-11-06 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511060900_202511060945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511061000_202511061045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-06 10:00", "2025-11-06 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511061000_202511061045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511061100_202511061145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-06 11:00", "2025-11-06 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511061100_202511061145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511061230_202511061315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-06 12:30", "2025-11-06 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511061230_202511061315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511130815_202511130900_dur_45_rm_gym1", "Physics", "9B", "2025-11-13 08:15", "2025-11-13 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511130815_202511130900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511130900_202511130945_dur_45_rm_a104", "Physics", "7C", "2025-11-13 09:00", "2025-11-13 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511130900_202511130945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511131000_202511131045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-13 10:00", "2025-11-13 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511131000_202511131045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511131100_202511131145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-13 11:00", "2025-11-13 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511131100_202511131145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511131230_202511131315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-13 12:30", "2025-11-13 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511131230_202511131315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511200815_202511200900_dur_45_rm_gym1", "Physics", "9B", "2025-11-20 08:15", "2025-11-20 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511200815_202511200900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511200900_202511200945_dur_45_rm_a104", "Physics", "7C", "2025-11-20 09:00", "2025-11-20 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511200900_202511200945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511201000_202511201045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-20 10:00", "2025-11-20 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511201000_202511201045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511201100_202511201145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-20 11:00", "2025-11-20 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511201100_202511201145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511201230_202511201315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-20 12:30", "2025-11-20 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511201230_202511201315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511270815_202511270900_dur_45_rm_gym1", "Physics", "9B", "2025-11-27 08:15", "2025-11-27 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511270815_202511270900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511270900_202511270945_dur_45_rm_a104", "Physics", "7C", "2025-11-27 09:00", "2025-11-27 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511270900_202511270945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511271000_202511271045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-27 10:00", "2025-11-27 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511271000_202511271045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511271100_202511271145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-27 11:00", "2025-11-27 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511271100_202511271145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511271230_202511271315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-27 12:30", "2025-11-27 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511271230_202511271315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202512040815_202512040900_dur_45_rm_gym1", "Physics", "9B", "2025-12-04 08:15", "2025-12-04 09:00", "45", "Gym1", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512040815_202512040900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202512040900_202512040945_dur_45_rm_a104", "Physics", "7C", "2025-12-04 09:00", "2025-12-04 09:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512040900_202512040945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202512041000_202512041045_dur_45_rm_a101", "Mathematics", "7A", "2025-12-04 10:00", "2025-12-04 10:45", "45", "A101", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512041000_202512041045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202512041100_202512041145_dur_45_rm_a103", "Mathematics", "8C", "2025-12-04 11:00", "2025-12-04 11:45", "45", "A103", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512041100_202512041145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512041230_202512041315_dur_45_rm_a102", "Mathematics", "7B", "2025-12-04 12:30", "2025-12-04 13:15", "45", "A102", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512041230_202512041315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_8a_202507250815_202507250900_dur_45_rm_a105", "Physics", "8A", "2025-07-25 08:15", "2025-07-25 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202507250815_202507250900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202507250900_202507250945_dur_45_rm_b204", "Chemistry", "8B", "2025-07-25 09:00", "2025-07-25 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202507250900_202507250945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202507251000_202507251045_dur_45_rm_b205", "Chemistry", "9A", "2025-07-25 10:00", "2025-07-25 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202507251000_202507251045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202507251100_202507251145_dur_45_rm_a104", "Physics", "7C", "2025-07-25 11:00", "2025-07-25 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202507251100_202507251145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202508010815_202508010900_dur_45_rm_a105", "Physics", "8A", "2025-08-01 08:15", "2025-08-01 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508010815_202508010900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202508010900_202508010945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-01 09:00", "2025-08-01 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508010900_202508010945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508011000_202508011045_dur_45_rm_b205", "Chemistry", "9A", "2025-08-01 10:00", "2025-08-01 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508011000_202508011045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202508011100_202508011145_dur_45_rm_a104", "Physics", "7C", "2025-08-01 11:00", "2025-08-01 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508011100_202508011145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202508080815_202508080900_dur_45_rm_a105", "Physics", "8A", "2025-08-08 08:15", "2025-08-08 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508080815_202508080900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202508080900_202508080945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-08 09:00", "2025-08-08 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508080900_202508080945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508081000_202508081045_dur_45_rm_b205", "Chemistry", "9A", "2025-08-08 10:00", "2025-08-08 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508081000_202508081045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202508081100_202508081145_dur_45_rm_a104", "Physics", "7C", "2025-08-08 11:00", "2025-08-08 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508081100_202508081145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202508150815_202508150900_dur_45_rm_a105", "Physics", "8A", "2025-08-15 08:15", "2025-08-15 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508150815_202508150900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202508150900_202508150945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-15 09:00", "2025-08-15 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508150900_202508150945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508151000_202508151045_dur_45_rm_b205", "Chemistry", "9A", "2025-08-15 10:00", "2025-08-15 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508151000_202508151045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202508151100_202508151145_dur_45_rm_a104", "Physics", "7C", "2025-08-15 11:00", "2025-08-15 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508151100_202508151145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202508220815_202508220900_dur_45_rm_a105", "Physics", "8A", "2025-08-22 08:15", "2025-08-22 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508220815_202508220900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202508220900_202508220945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-22 09:00", "2025-08-22 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508220900_202508220945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508221000_202508221045_dur_45_rm_b205", "Chemistry", "9A", "2025-08-22 10:00", "2025-08-22 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508221000_202508221045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202508221100_202508221145_dur_45_rm_a104", "Physics", "7C", "2025-08-22 11:00", "2025-08-22 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508221100_202508221145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202508290815_202508290900_dur_45_rm_a105", "Physics", "8A", "2025-08-29 08:15", "2025-08-29 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202508290815_202508290900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202508290900_202508290945_dur_45_rm_b204", "Chemistry", "8B", "2025-08-29 09:00", "2025-08-29 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202508290900_202508290945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202508291000_202508291045_dur_45_rm_b205", "Chemistry", "9A", "2025-08-29 10:00", "2025-08-29 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202508291000_202508291045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202508291100_202508291145_dur_45_rm_a104", "Physics", "7C", "2025-08-29 11:00", "2025-08-29 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202508291100_202508291145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202509050815_202509050900_dur_45_rm_a105", "Physics", "8A", "2025-09-05 08:15", "2025-09-05 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509050815_202509050900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202509050900_202509050945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-05 09:00", "2025-09-05 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509050900_202509050945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509051000_202509051045_dur_45_rm_b205", "Chemistry", "9A", "2025-09-05 10:00", "2025-09-05 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509051000_202509051045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202509051100_202509051145_dur_45_rm_a104", "Physics", "7C", "2025-09-05 11:00", "2025-09-05 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509051100_202509051145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202509120815_202509120900_dur_45_rm_a105", "Physics", "8A", "2025-09-12 08:15", "2025-09-12 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509120815_202509120900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202509120900_202509120945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-12 09:00", "2025-09-12 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509120900_202509120945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509121000_202509121045_dur_45_rm_b205", "Chemistry", "9A", "2025-09-12 10:00", "2025-09-12 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509121000_202509121045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202509121100_202509121145_dur_45_rm_a104", "Physics", "7C", "2025-09-12 11:00", "2025-09-12 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509121100_202509121145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202509190815_202509190900_dur_45_rm_a105", "Physics", "8A", "2025-09-19 08:15", "2025-09-19 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509190815_202509190900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202509190900_202509190945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-19 09:00", "2025-09-19 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509190900_202509190945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509191000_202509191045_dur_45_rm_b205", "Chemistry", "9A", "2025-09-19 10:00", "2025-09-19 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509191000_202509191045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202509191100_202509191145_dur_45_rm_a104", "Physics", "7C", "2025-09-19 11:00", "2025-09-19 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509191100_202509191145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202509260815_202509260900_dur_45_rm_a105", "Physics", "8A", "2025-09-26 08:15", "2025-09-26 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202509260815_202509260900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202509260900_202509260945_dur_45_rm_b204", "Chemistry", "8B", "2025-09-26 09:00", "2025-09-26 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202509260900_202509260945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202509261000_202509261045_dur_45_rm_b205", "Chemistry", "9A", "2025-09-26 10:00", "2025-09-26 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202509261000_202509261045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202509261100_202509261145_dur_45_rm_a104", "Physics", "7C", "2025-09-26 11:00", "2025-09-26 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202509261100_202509261145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202510030815_202510030900_dur_45_rm_a105", "Physics", "8A", "2025-10-03 08:15", "2025-10-03 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510030815_202510030900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202510030900_202510030945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-03 09:00", "2025-10-03 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510030900_202510030945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510031000_202510031045_dur_45_rm_b205", "Chemistry", "9A", "2025-10-03 10:00", "2025-10-03 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510031000_202510031045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202510031100_202510031145_dur_45_rm_a104", "Physics", "7C", "2025-10-03 11:00", "2025-10-03 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510031100_202510031145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202510100815_202510100900_dur_45_rm_a105", "Physics", "8A", "2025-10-10 08:15", "2025-10-10 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510100815_202510100900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202510100900_202510100945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-10 09:00", "2025-10-10 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510100900_202510100945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510101000_202510101045_dur_45_rm_b205", "Chemistry", "9A", "2025-10-10 10:00", "2025-10-10 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510101000_202510101045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202510101100_202510101145_dur_45_rm_a104", "Physics", "7C", "2025-10-10 11:00", "2025-10-10 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510101100_202510101145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202510170815_202510170900_dur_45_rm_a105", "Physics", "8A", "2025-10-17 08:15", "2025-10-17 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510170815_202510170900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202510170900_202510170945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-17 09:00", "2025-10-17 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510170900_202510170945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510171000_202510171045_dur_45_rm_b205", "Chemistry", "9A", "2025-10-17 10:00", "2025-10-17 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510171000_202510171045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202510171100_202510171145_dur_45_rm_a104", "Physics", "7C", "2025-10-17 11:00", "2025-10-17 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510171100_202510171145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202510240815_202510240900_dur_45_rm_a105", "Physics", "8A", "2025-10-24 08:15", "2025-10-24 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510240815_202510240900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202510240900_202510240945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-24 09:00", "2025-10-24 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510240900_202510240945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510241000_202510241045_dur_45_rm_b205", "Chemistry", "9A", "2025-10-24 10:00", "2025-10-24 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510241000_202510241045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202510241100_202510241145_dur_45_rm_a104", "Physics", "7C", "2025-10-24 11:00", "2025-10-24 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510241100_202510241145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202510310815_202510310900_dur_45_rm_a105", "Physics", "8A", "2025-10-31 08:15", "2025-10-31 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202510310815_202510310900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202510310900_202510310945_dur_45_rm_b204", "Chemistry", "8B", "2025-10-31 09:00", "2025-10-31 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202510310900_202510310945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202510311000_202510311045_dur_45_rm_b205", "Chemistry", "9A", "2025-10-31 10:00", "2025-10-31 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202510311000_202510311045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202510311100_202510311145_dur_45_rm_a104", "Physics", "7C", "2025-10-31 11:00", "2025-10-31 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202510311100_202510311145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511070815_202511070900_dur_45_rm_a105", "Physics", "8A", "2025-11-07 08:15", "2025-11-07 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511070815_202511070900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511070900_202511070945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-07 09:00", "2025-11-07 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511070900_202511070945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511071000_202511071045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-07 10:00", "2025-11-07 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511071000_202511071045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511071100_202511071145_dur_45_rm_a104", "Physics", "7C", "2025-11-07 11:00", "2025-11-07 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511071100_202511071145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511140815_202511140900_dur_45_rm_a105", "Physics", "8A", "2025-11-14 08:15", "2025-11-14 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511140815_202511140900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511140900_202511140945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-14 09:00", "2025-11-14 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511140900_202511140945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511141000_202511141045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-14 10:00", "2025-11-14 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511141000_202511141045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511141100_202511141145_dur_45_rm_a104", "Physics", "7C", "2025-11-14 11:00", "2025-11-14 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511141100_202511141145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511210815_202511210900_dur_45_rm_a105", "Physics", "8A", "2025-11-21 08:15", "2025-11-21 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511210815_202511210900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511210900_202511210945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-21 09:00", "2025-11-21 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511210900_202511210945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511211000_202511211045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-21 10:00", "2025-11-21 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511211000_202511211045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511211100_202511211145_dur_45_rm_a104", "Physics", "7C", "2025-11-21 11:00", "2025-11-21 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511211100_202511211145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511280815_202511280900_dur_45_rm_a105", "Physics", "8A", "2025-11-28 08:15", "2025-11-28 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511280815_202511280900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511280900_202511280945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-28 09:00", "2025-11-28 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511280900_202511280945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511281000_202511281045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-28 10:00", "2025-11-28 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511281000_202511281045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511281100_202511281145_dur_45_rm_a104", "Physics", "7C", "2025-11-28 11:00", "2025-11-28 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511281100_202511281145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202512050815_202512050900_dur_45_rm_a105", "Physics", "8A", "2025-12-05 08:15", "2025-12-05 09:00", "45", "A105", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512050815_202512050900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202512050900_202512050945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-05 09:00", "2025-12-05 09:45", "45", "B204", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512050900_202512050945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512051000_202512051045_dur_45_rm_b205", "Chemistry", "9A", "2025-12-05 10:00", "2025-12-05 10:45", "45", "B205", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512051000_202512051045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202512051100_202512051145_dur_45_rm_a104", "Physics", "7C", "2025-12-05 11:00", "2025-12-05 11:45", "45", "A104", "sc_joni1");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512051100_202512051145_dur_45_rm_a104");
    """)
    conn.commit()          # <-- add this
except Exception as e:
    conn.rollback()        # good hygiene
    raise
finally:
    conn.close()
