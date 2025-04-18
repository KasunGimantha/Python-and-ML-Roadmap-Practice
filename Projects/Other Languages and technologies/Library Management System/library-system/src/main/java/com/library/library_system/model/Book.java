package com.library.library_system.model;

import jakarta.persistence.*;
import lombok.*;

@Entity //Marks the JPA entry
@Data //generate getters,setters
@NoArgsConstructor //generate a no args constructoir
@AllArgsConstructor //generate an all args constructor
@Builder  //enable builder pattern for the clas

public class Book {
    @Id //Specify the primary key
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String title;

    @Column(nullable = false)
    private String author;

    @Column(unique = true)
    private String isbn;

    @Column(nullable = false)
    private String status = "Available";

}
