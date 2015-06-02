package com.zzm.interview;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HorseRunTest {

    @Test
    public void should_find_horse_shortest_run_correct() throws Exception {
        assertEquals(2, new HorseRun(new Point(1, 1), new Point(4, 4)).find());
        assertEquals(5, new HorseRun(new Point(1, 2), new Point(7, 9)).find());
    }

}