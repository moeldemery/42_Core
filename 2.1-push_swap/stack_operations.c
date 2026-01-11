/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_operations.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 17:14:25 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 17:14:28 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void    ft_stack_swap(t_list **stack)
{
    t_list *first;
    t_list *second;

    if (!stack || !*stack || !(*stack)->next)
        return;
    first = *stack;
    second = (*stack)->next;
    first->next = second->next;
    second->next = first;
    *stack = second;
}

void    ft_stack_push(t_list **src, t_list **dest)
{
    t_list *temp;

    if (!src || !*src)
        return;
    temp = *src;
    *src = (*src)->next;
    temp->next = *dest;
    *dest = temp;
}

void    ft_stack_rotate(t_list **stack)
{
    t_list *first;
    t_list *last;

    if (!stack || !*stack || !(*stack)->next)
        return;
    first = *stack;
    *stack = (*stack)->next;
    first->next = NULL;
    last = *stack;
    while (last->next)
        last = last->next;
    last->next = first;
}

void    ft_stack_reverse_rotate(t_list **stack)
{
    t_list *prev;
    t_list *last;

    if (!stack || !*stack || !(*stack)->next)
        return;
    prev = NULL;
    last = *stack;
    while (last->next)
    {
        prev = last;
        last = last->next;
    }
    prev->next = NULL;
    last->next = *stack;
    *stack = last;
}