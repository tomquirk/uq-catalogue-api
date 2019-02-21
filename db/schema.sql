--
-- PostgreSQL database dump
--
-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;

SET lock_timeout = 0;

SET idle_in_transaction_session_timeout = 0;

SET client_encoding = 'UTF8';

SET standard_conforming_strings = ON;

SET check_function_bodies = FALSE;

SET client_min_messages = warning;

SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = FALSE;

--
-- Name: course; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE course (
    course_code character (8) NOT NULL,
    title character varying (100),
    description text,
    raw_prerequisites text,
    units integer,
    semester_1 boolean,
    semester_2 boolean,
    summer_semester boolean,
    not_offered boolean
);

CREATE TABLE course_profile (
    course_profile_id integer,
    course_code character (8) NOT NULL
);

--
-- Name: course_assessment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE course_assessment (
    id SERIAL,
    course_profile_id integer,
    assessment_name text,
    due_date timestamp,
    weighting float,
    learning_obj text
);
--
-- Name: incompatible_courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE incompatible_courses (
    course_code character varying (8) NOT NULL,
    incompatible_course_code character varying (8) NOT NULL
);

--
-- Name: plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE plan (
    plan_code character (10) NOT NULL,
    title character (100) NOT NULL
);

--
-- Name: plan_to_program; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE plan_to_program (
    plan_code character (10) NOT NULL,
    program_code character (4) NOT NULL
);

--
-- Name: course_to_plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE course_to_plan (
    course_code character (8) NOT NULL,
    plan_code character (10) NOT NULL,
    required boolean
);

--
-- Name: program; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE program (
    program_code character (4) NOT NULL,
    title character (100),
    level character (45),
    abbreviation character (40),
    duration_years integer,
    units integer
);

--
-- Name: course_to_program; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE course_to_program (
    course_code character (8) NOT NULL,
    program_code character (4) NOT NULL
);

--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_code);

--
-- Name: incompatible_courses incompatible_courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT incompatible_courses_pkey PRIMARY KEY (course_code, incompatible_course_code);

--
-- Name: course_to_plan course_to_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_plan
    ADD CONSTRAINT course_to_plan_pkey PRIMARY KEY (course_code, plan_code);

--
-- Name: plan planpk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan
    ADD CONSTRAINT planpk PRIMARY KEY (plan_code);

--
-- Name: plan plan_to_program_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan_to_program
    ADD CONSTRAINT plan_to_program_pk PRIMARY KEY (plan_code, program_code);

--
-- Name: plan plan_to_program_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_profile
    ADD CONSTRAINT course_profile_pk PRIMARY KEY (course_profile_id);

--
-- Name: course_to_program course_to_program_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_program
    ADD CONSTRAINT course_to_program_pkey PRIMARY KEY (course_code, program_code);

--
-- Name: program program_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY program
    ADD CONSTRAINT program_pkey PRIMARY KEY (program_code);

--
-- Name: course_to_plan course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_profile
    ADD CONSTRAINT "course.course_code" FOREIGN KEY (course_code) REFERENCES course (course_code) ON DELETE CASCADE;

--
-- Name: course_assessment course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_assessment
    ADD CONSTRAINT "course_profile.course_profile_id"
    FOREIGN KEY (course_profile_id)
    REFERENCES course_profile (course_profile_id)
    ON DELETE CASCADE;

--
-- Name: course_to_plan course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_plan
    ADD CONSTRAINT "course.course_code" FOREIGN KEY (course_code) REFERENCES course (course_code);

--
-- Name: course_to_plan course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan_to_program
    ADD CONSTRAINT "plan.plan_code" FOREIGN KEY (plan_code) REFERENCES plan (plan_code);

--
-- Name: incompatible_courses course_code_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT course_code_fk FOREIGN KEY (course_code) REFERENCES course (course_code);

--
-- Name: course_to_program coursecodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_program
    ADD CONSTRAINT coursecodefk FOREIGN KEY (course_code) REFERENCES course (course_code);

--
-- Name: incompatible_courses i_course_code_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT i_course_code_fk FOREIGN KEY (incompatible_course_code) REFERENCES course (course_code);

--
-- Name: course_to_plan plancodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_plan
    ADD CONSTRAINT plancodefk FOREIGN KEY (plan_code) REFERENCES plan (plan_code);

--
-- Name: course_to_program programcodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course_to_program
    ADD CONSTRAINT programcodefk FOREIGN KEY (program_code) REFERENCES program (program_code);

--
-- PostgreSQL database dump complete
--
